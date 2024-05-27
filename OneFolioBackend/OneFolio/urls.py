from django.urls import path
from . import views

urlpatterns = [
    path('users/view', views.user_view, name='users'),
    path('investments/view', views.investment_view, name='investments'),
    path('users/', views.user_list, name='user_list'),
    path('users/<str:user_id>/', views.user_detail, name='user_detail'),
    path('users/email/<str:email>/', views.user_by_email, name='user_by_email'),
    
    # Investment endpoints
    path('investments/', views.investment_list, name='investment_list'),
    path('investments/<str:investment_id>/', views.investment_detail, name='investment_detail'),
]
