from django.contrib import admin
from tcf14.models import Company, Booth

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

# Register Admin Information
admin.site.register(Company, CompanyAdmin)
admin.site.register(Booth, BoothAdmin)