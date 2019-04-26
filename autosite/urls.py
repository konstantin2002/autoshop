"""autosite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from autosite import views
from cars import car_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^registration/', views.register_user),
    url(r'^login/', views.log_in),
    url(r'^search2/', views.search2),
    url(r'^search/', views.search),
    url(r'^load_brand/load_mod/load_engine/load_year', car_views.get_year),
    url(r'^load_brand/load_mod/load_engine', car_views.get_engine),
    url(r'^load_brand/load_mod/', car_views.get_mod),
    url(r'^load_brand/', car_views.get_brand),
    url(r'^exp/', views.exp),
    url(r'^contact/thanks/', views.contact_thanks),
    url(r'^contact/$', views.contact),
    url(r'^contact/(?P<num>\d{2})/$', views.contact),
    url(r'^pb/([^/]+)/$', views.pushed_button),
]
