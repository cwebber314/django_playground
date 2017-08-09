from django.conf.urls import url, include
from django_filters.views import FilterView

from . import views
from .models import Branch

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^branches/$', views.BranchView.as_view(), name='branches'),
    url(r'^lines/$', views.lines, name='lines'),
    url(r'^equipment/$', views.equipment, name='equipment'),
    url(r'^select2/', include('django_select2.urls')), # for ModelWidgets.
]
