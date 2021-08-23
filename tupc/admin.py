from django.contrib import admin
from .models import OrganizationInfo, OfficersInfo, ActivitiesInfo, ReportsInfo

#Register your models here.
admin.site.register(OrganizationInfo)
admin.site.register(OfficersInfo)
admin.site.register(ActivitiesInfo)
admin.site.register(ReportsInfo)
