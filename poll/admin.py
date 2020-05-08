from django.contrib import admin
from .models import profile,certificates
from .models import checking
admin.site.register(profile)
admin.site.register(checking)
admin.site.register(certificates)