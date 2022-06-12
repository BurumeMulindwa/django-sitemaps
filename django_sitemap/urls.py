# urls.py
from django.contrib import admin
from django.contrib.sitemaps import GenericSitemap  # new
from django.contrib.sitemaps.views import sitemap  # new
from django.urls import path, include

from myapp.models import Snippet  # new

info_dict = {
    'queryset': Snippet.objects.all(),
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('sitemap.xml', sitemap,  # new
         {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
         name='django.contrib.sitemaps.views.sitemap'),
]
