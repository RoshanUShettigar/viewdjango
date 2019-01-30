from django.conf.urls import url
from . import views

app_name='personinfo'


urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^personinfo/add/$', views.Infosave.as_view(), name='saves'),
    url(r'personinfo/(?P<pk>[0-9]+)/$', views.editInfo.as_view(), name="edit"),
    url(r'personinfo/(?P<pk>[0-9]+)/delete/$', views.deleteInfo.as_view(), name="deletes"),

]