# noinspection PyUnresolvedReferences,PyPackageRequirements
from blogging.models import Post, Category
from django.contrib import admin

admin.site.register(Post)
admin.site.register(Category)
