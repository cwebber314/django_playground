from django.conf.urls import url, include
from django_filters.views import FilterView

from . import views
from .models import Branch

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lines/$', views.lines, name='lines'),
    url(r'^branches/$', views.BranchesView.as_view(), name='branches'),
    url(r'^branches2/$', views.branches2, name='branches2'),
    url(r'^equipment/$', views.equipment, name='equipment'), # Render manually
    url(r'^equipment2/$', views.equipment2, name='equipment2'), # Render manually with data tables
    url(r'^equipment3/$', views.equipment3, name='equipment3'), # Editable
    url(r'^equipment4/$', views.equipment4, name='equipment4'), # Editable
    url(r'^equipment5/$', views.equipment5, name='equipment5'), # Editable
    url(r'^equipment/edit/(?P<pk>[0-9]+)/$', views.EquipmentUpdate.as_view()),
    url(r'^select2/', include('django_select2.urls')), # for ModelWidgets.
    url(r'^branch/update/(?P<pk>[0-9]+)/$', views.BranchUpdate.as_view()),
    url(r'^branch/up/(?P<pk>[0-9]+)/$', views.BranchView.as_view()),
    #url(r'^branch/show/(?P<pk>[0-9]+)/$', views.BranchShow.as_view()),
    url(r'^branch/create/(?P<pk>[0-9]+)/$', views.BranchCreate.as_view()),
    url(r'^branchlist/$', views.BranchList.as_view()),
]
