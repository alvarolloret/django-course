from django.contrib import admin

from users_app.models import User, UserAge
# Register your models here.

#python manage.py createsuperuser
#username: alvaro_lloret@hotmail.com
#password: aloa6527


admin.site.register(User)
admin.site.register(UserAge)
