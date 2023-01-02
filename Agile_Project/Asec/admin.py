from django.contrib import admin

# Register your models here.=
from .models import Role
from .models import User
from .models import Tracker
from .models import Urls
from .models import Committee
# Register your models here.
admin.site.register(Role)
admin.site.register(User)
admin.site.register(Tracker)
admin.site.register(Urls)
admin.site.register(Committee)
