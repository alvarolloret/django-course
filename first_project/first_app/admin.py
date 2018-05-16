from django.contrib import admin
#lecture 127
from first_app.models import AccesRecord, Topic, Webpage
# Register your models here.

#python manage.py createsuperuser
#username: alvaro_lloret@hotmail.com
#password: aloa6527


admin.site.register(AccesRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
