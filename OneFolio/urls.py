from django.urls import path
from . import views

urlpatterns = [
    path('users/view', views.user_view, name='users'),
    path('investments/view', views.investment_view, name='investments'),
    path('users/', views.user_list, name='user_list'),
    path('users/<str:user_id>/', views.user_detail, name='user_detail'),
    path('users/email/<str:email>/', views.user_by_email, name='user_by_email'),
    path('users/investments/<str:user_id>/', views.investments_by_user, name='investments_by_user'),
    
    # Investment endpoints
    path('investments/', views.investment_list, name='investment_list'),
    path('investments/addMany', views.investment_list_many, name='investment_list_many'),
    path('investments/<str:investment_id>/', views.investment_detail, name='investment_detail'),

    #API Banking
    path('users/<str:user_id>/cursor', views.cursor_detail, name='cursor_detail'),

]
