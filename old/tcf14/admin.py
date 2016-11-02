from django.contrib import admin
from tcf14.models import Company, Booth, Visit, Checkin

class CompanyAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic Information',    {'fields': ['name', 'description', 'logo']}),
        ('Contact Information', {'fields': ['website', 'facebook', 'twitter', 'linkedin', 'email']}),
        ('Booth Information', {'fields': ['booth']}),
    ]
    list_display = ('name', 'booth')
    search_fields = ['name']
    ordering = ['name']

class BoothAdmin(admin.ModelAdmin):
    list_display = ('number', 'company', 'row', 'col')
    ordering = ['number']

    def company(self, instance):
        try:
            return instance.company.name
        except Company.DoesNotExist:
            return "N/A"

class VisitAdmin(admin.ModelAdmin):
    list_display = ('date', 'company', 'ip', 'user')
    ordering = ['date']

    list_filter = ['company', 'user']

class CheckInAdmin(admin.ModelAdmin):
    list_display = ('date', 'company', 'user')
    ordering = ['date']

    list_filter = ['company', 'user']

# Register Admin Information
admin.site.register(Company, CompanyAdmin)
admin.site.register(Booth, BoothAdmin)
admin.site.register(Visit, VisitAdmin)
admin.site.register(Checkin, CheckInAdmin)