from django.conf.urls import url
from drones import views

urlpatterns = [
    url(r'^drones-categories/$', views.DronesCategoryList.as_view(),
        name=views.DronesCategoryList.name),
    url(r'^drones-categories/(?P<pk>[0-9]+)$', views.DronesCategoryDetail.as_view(
    ), name=views.DronesCategoryDetail.name),
    url(r'^drones/$', views.DroneList.as_view(), name=views.DroneList.name),
    url(r'^drones/(?P<pk>[0-9]+)$',
        views.DroneDetail.as_view(), name=views.DroneDetail.name),
    url(r'^pilots/$', views.PilotList.as_view(), name=views.PilotList.name),
    url(r'^pilots/(?P<pk>[0-9]+)$',
        views.PilotDetail.as_view(), name=views.PilotDetail.name),
    url(r'^competitions/$', views.CompetitionList.as_view(),
        name=views.CompetitionList.name),
    url(r'^competitions/(?P<pk>[0-9]+)$',
        views.CompetitionDetail.as_view(), name=views.CompetitionDetail.name),
    url(r'^$', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]
