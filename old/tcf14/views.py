from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404, render_to_response
from django.http import Http404
from django.views import generic
from ipware.ip import get_ip_address_from_request
from tcf14.models import *

def index(request):
	return render_to_response('mobile/index.html')

def map(request, id = "0"):
	rows = Booth.objects.values("row").distinct().order_by("row")
	context = []

	for row_data in rows:
		orm_data = Booth.objects.filter(row=row_data['row']).order_by("col")
		context.extend([orm_data])

	return render_to_response('mobile/map.html', { 'row_data': context, 'highlight': int(id) })

def privacy(request):
	return render_to_response('mobile/privacy.html')
	
def help(request):
	return render_to_response('mobile/help.html')

def booth(request, id):
	booth = get_object_or_404(Booth, id=id)

	try:
		company = booth.company
		return redirect('company', pk=company.id)
	except Company.DoesNotExist:
		raise Http404

@login_required
def checkin(request, id):
	company = get_object_or_404(Company, id=id)
	user = request.user
	Checkin.objects.create_checkin(company, user)
	return redirect('company', pk=id)

class ListView(generic.ListView):
	template_name = 'mobile/list.html'
	context_object_name = 'company_list'
	model = Company

	def get_queryset(self):
		return Company.objects.all().order_by('name')

class CompanyView(generic.DetailView):
	template_name = 'mobile/company.html'
	model = Company
	user = None
	ip = None
	company = None

	def dispatch(self, request, *args, **kwargs):
		self.user = request.user
		self.ip = get_ip_address_from_request(request)
		return super(CompanyView, self).dispatch(request, *args, **kwargs)

	def get_object(self, queryset=None):
		self.company = super(CompanyView, self).get_object(queryset)
		
		if self.user.is_authenticated():
			Visit.objects.create_auth_visit(self.company, self.user, self.ip)
		else:
			Visit.objects.create_visit(self.company, self.ip)

		return self.company

	def get_context_data(self, **kwargs):
	    context = super(CompanyView, self).get_context_data(**kwargs)

	    try:
			if self.user.is_authenticated():
				checkin = Checkin.objects.filter(company=self.company).get(user=self.user)
				context['checkin'] = checkin
			else:
				context['checkin'] = True
	    except Checkin.DoesNotExist:
	    	context['checkin'] = False

	    return context