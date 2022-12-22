from django.contrib import admin

# Register your models here.
from .models import Committee_des
from .models import Role
from .models import User
from .models import Tracker
# Register your models here.
admin.site.register(Committee_des)
admin.site.register(Role)
admin.site.register(User)
admin.site.register(Tracker)

