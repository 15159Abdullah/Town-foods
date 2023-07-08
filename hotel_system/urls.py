from hotel_system import views
from django.urls import path 


urlpatterns = [
    path('home_page/', views.home_page , name="home_page"),
    path('contact_us/',views.contact_us,name='contact_us'),
    path('rooms/',views.rooms,name='rooms'),
    path('about_us/',views.about_us, name='about_us'),
    path('restaurant/',views.restaurant,name='restaurant'),
    path('room_detail_page/<pk>/',views.room_detail_page,name='room_detail_page'),
    path('order/',views.Order,name='order'), 
   
] 
