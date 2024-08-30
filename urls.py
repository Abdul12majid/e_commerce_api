from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("products", views.ApiProducts)

urlpatterns = router.urls

#urlpatterns = [
	#path('all-products', views.ApiProducts.as_view()),
	#path('product-info/<int:pk>', views.Apiproduct.as_view()),
	#path('update-info', views.update_info),
#]

