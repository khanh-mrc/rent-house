from django.urls import path

from . import views

urlpatterns = [
    path('listings/test',views.test),
    path('listings/',views.listing_list,name='listings'),
    #path('listings/<pk>/',views.listing_retrieve,name='detail'),
    path('search',views.search,name = "search"),
    path('listings/<int:listing_id>/', views.listing_retrieve, name='listing'),

]