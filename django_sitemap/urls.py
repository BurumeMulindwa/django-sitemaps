
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from myapp.sitemaps import StaticViewSitemap


sitemaps = {
    'static': StaticViewSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('', include('myapp.urls')),
]
