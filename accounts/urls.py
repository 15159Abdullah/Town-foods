
from django.urls import path
from accounts import views

urlpatterns = [
    path('admin_login/', views.admin_login, name='admin_login' ),
    path('admin_signup/', views.admin_signup, name='admin_signup' ),
    path('admin_logout/', views.admin_logout, name='admin_logout' ),
    path('customer_sign_up/', views.customer_sign_up , name="customer_sign_up"),
    path('customer_log_in/', views.customer_log_in , name="customer_log_in"),
    path('customer_log_out/', views.customer_log_out , name="customer_log_out"),
    
]