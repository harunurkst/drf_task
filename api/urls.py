from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^contact/$', views.ContactList.as_view()),  # Contact list url
    url(r'^contact/(?P<pk>[0-9]+)$', views.ContactDetail.as_view()),  # Contact detail url
]

urlpatterns = format_suffix_patterns(urlpatterns)
