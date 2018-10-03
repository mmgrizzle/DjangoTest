"""
Definition of urls for DjangoTest.
"""

from django.conf.urls import include, url
import AppTest.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

#urlpatterns = [
    # Examples:
    # url(r'^$', DjangoTest.views.home, name='home'),
    # url(r'^DjangoTest/', include('DjangoTest.DjangoTest.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
#]

urlpatterns = [
    url(r'^$', AppTest.views.index, name='index'), #routes to .com/
    url(r'^home$', AppTest.views.index, name='home'), #routes to .com/home
]