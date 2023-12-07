from django.contrib import admin

# noinspection PyUnresolvedReferences,PyPackageRequirements
from polling.models import Poll

admin.site.register(Poll)
