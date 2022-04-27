from . import views
from django.urls import path
from django.conf import settings  
from django.conf.urls.static import static  

urlpatterns = [
    path('',views.products, name="home"),
    path('products/',views.products, name="products"),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('success/', views.successView), 
    path('cancelled/', views.CancelledView.as_view()),
    path('webhook/', views.stripe_webhook), 
    path('mycart/', views.mycart,name="mycart"), 
    path('add_products/',views.add_products,name="add_products"),
    path('view_cart/',views.view_cart,name="view_cart"),
    path('deletedata/',views.deletedata,name="deletedata")
]
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  

