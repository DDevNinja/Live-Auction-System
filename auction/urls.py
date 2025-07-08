from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuctionViewSet, BidViewSet, WalletViewSet, test_view

router = DefaultRouter()
router.register(r'auctions', AuctionViewSet)
router.register(r'bids', BidViewSet)
router.register(r'wallets', WalletViewSet)

urlpatterns = [
    path('test/', test_view, name='test_view'),
    path('', include(router.urls)),
]
