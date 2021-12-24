from django.urls import path
from . import views

urlpatterns = [
    path("admin_panel/", views.adminLte, name='adminLte'),
    path("admin_panel/<str:name>", views.charts, name='charts'),
    path("admin_panel/msg/<str:mailbox_name>", views.mailbox, name='mailbox'),
    path("admin_panel/msg/mailbox/<int:inbox_id>", views.mailbox_imbox_detail, name='mailbox_imbox_detail'),
]