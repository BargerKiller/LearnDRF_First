from rest_framework.routers import DefaultRouter


from products.viewsets import ProductViewSet, ProductGenericViewSet

router = DefaultRouter()
router.register('product-abs', ProductGenericViewSet, basename="products")

urlpatterns = router.urls
