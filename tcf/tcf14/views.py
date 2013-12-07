from django.shortcuts import redirect, get_object_or_404, render_to_response
from django.http import Http404
from django.views import generic
from ipware.ip import get_ip_address_from_request
from tcf14.models import *

def index(request):
	return render_to_response('index.html')

def map(request, id = "0"):
	rows = Booth.objects.values("row").distinct().order_by("row")
	context = []

	for row_data in rows:
		orm_data = Booth.objects.filter(row=row_data['row']).order_by("col")
		context.extend([orm_data])

	return render_to_response('map.html', { 'row_data': context, 'highlight': int(id) })

def privacy(request):
	return render_to_response('privacy.html')

def booth(request, id):
	booth = get_object_or_404(Booth, id=id)

	try:
		company = booth.company
		return redirect('company', pk=company.id)
	except Company.DoesNotExist:
		raise Http404

class ListView(generic.ListView):
	template_name = 'list.html'
	context_object_name = 'company_list'
	model = Company

	def get_queryset(self):
		return Company.objects.all().order_by('name')

class CompanyView(generic.DetailView):
	template_name = 'company.html'
	model = Company
	user = None
	ip = None

	def dispatch(self, request, *args, **kwargs):
		self.user = request.user
		self.ip = get_ip_address_from_request(request)
		return super(CompanyView, self).dispatch(request, *args, **kwargs)

	def get_object(self, queryset=None):
		company = super(CompanyView, self).get_object(queryset)
		
		if self.user.is_authenticated():
			Visit.objects.create_auth_visit(company, self.user, self.ip)
		else:
			Visit.objects.create_visit(company, self.ip)

		return company