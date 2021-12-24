from django.conf.urls.static import static
from django.urls import path
from SmartOne import settings
from . import views

urlpatterns = [
    path("products/", views.store, name='store'),
    path("cart/", views.cart, name='cart'),
    path('click/transaction/', views.TestView.as_view(), name='transaction'),
    path("checkout/", views.checkout, name='checkout'),
    path('click/transaction/', views.TestView.as_view()),
    path("update_item/", views.update_item, name='update_item'),
    path("process_order/", views.processOrder, name='process_order'),
    path("paycom_payment/", views.Payment.as_view(), name='paycom_payment'),
    path("success_payment/<int:status><str:payment_id>", views.success_payment, name='success_payment'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
