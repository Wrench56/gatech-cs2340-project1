from django.contrib import admin

from movies.models import *

admin.site.register(Person)
admin.site.register(Movie)
