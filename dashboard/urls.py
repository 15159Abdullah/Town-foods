
from django.urls import path
from dashboard import views

urlpatterns = [
    path('home/', views.home, name='home' ),

    path('invoice_list/', views.invoice_list, name='invoice_list' ),
    path('invoice_view/<pk>/', views.invoice_view, name='invoice_view' ),
    path('delete_invoice/<pk>/', views.delete_invoice, name='delete_invoice' ),
    
    #..........Roooms.................

    path('rooms_list/', views.rooms_list, name='rooms_list' ),
    path('add_room/', views.add_room, name='add_room' ),
    path('delete_room/<pk>/', views.delete_room, name='delete_room' ),
    path('update_room/<pk>/', views.update_room, name='update_room' ),
   
    #...........Foods..................

    path('foods_list/', views.foods_list, name='foods_list' ),
    path('add_food/', views.add_food, name='add_food' ),
    path('delete_food/<pk>/', views.delete_food, name='delete_food' ),
    path('update_food/<pk>/', views.update_food, name='update_food' ),
   

    path('orders_list/', views.orders_list, name='orders_list' ),
    path('delete_order/<pk>/', views.delete_order, name='delete_order' ),
   
    #...........Contact Us..................
    
    path('contact_list/', views.contact_list, name='contact_list' ),
    path('delete_contact/<pk>/', views.delete_contact, name='delete_contact' ),
   

    #.............Users.......................

    path('user_list/', views.user_list, name='user_list' ),
    path('delete_user/<pk>/', views.delete_user, name='delete_user' ),
   
   

]