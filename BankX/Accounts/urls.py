from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('account_overview/', views.account_overview, name='account_overview'),
    path('create_account/', views.create_account, name='create_account'),
    path('create_account', views.create_account, name='create_account'),
    path('deposit/', views.deposit, name='deposit'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('list_accounts/', views.list_accounts, name='list_accounts'),
]