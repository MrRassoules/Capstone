from django.contrib import admin
from .models import *
# Import models from csv
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Create the State Demographic resource
class StateDemographicResource(resources.ModelResource):
	class Meta:
		model = StateDemographic
		
# Let the admin page know that the resouce is the state demographic resource
class StateDemographicAdmin(ImportExportModelAdmin):
	resource_class = StateDemographicResource
	list_display = ('state', )
	

# Register the StateDemographics table
admin.site.register(StateDemographic, StateDemographicAdmin)

