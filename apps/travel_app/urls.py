from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^dashboard', views.dashboard),     
    url(r'^add/', views.create_trip),     
    url(r'^join/', views.join_trip),     
    url(r'^destination/(?P<trip_id>\d+)$', views.show_trip),     
    url(r'^process_create_trip/', views.process_create_trip),     
]
