from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
    #login/logout
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),

    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),

    #query room
    url(r'^query_room/$', views.query_room, name='query_room'),
    #order room
    url(r'^BookingRoom/$', views.booking_room, name='booking_room'),
    #checkout
    url(r'^checkout/$', views.checkout, name='checkout'),
    #checkin
    url(r'^checkin/$', views.checkin, name='checkin'),
    #test View
    url(r'^order/(?P<pk>[0-9]+)/$', views.OrderView.as_view(), name='order'),
    #initial_models
    url(r'^initialModels/', views.initial_models, name='initial_models'),
    url(r'^createModelsData/', views.create_models_data, name='create_models_data'),
]
