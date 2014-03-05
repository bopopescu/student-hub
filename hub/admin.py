import logging
from django.contrib import admin
from hub.models import *
from django.contrib.auth.models import User

class StudentAdmin(admin.ModelAdmin):
    model=Student
    fieldsets=[
        ('User', {'fields':['user']}),
        ('Info', {'fields':['listed','latitude','longitude', 'degree' ,'bio','picture', 'city', 'country','facebook_link']}),

	]

    list_display = ['last_name']
    def last_name(self, instance):
        return instance.user.last_name
admin.site.register(Student, StudentAdmin)
