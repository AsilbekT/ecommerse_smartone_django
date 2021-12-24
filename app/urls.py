from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("service/", views.service, name='service'),
    path("about/", views.about, name='about'),
    path("messages/", views.messages, name='messages'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/login/', views.login_page, name='login'),
    path("accounts/logout/", views.logout_user, name="logout"),
    path("messages/<int:id>", views.message_detail, name='message_detail')
]
