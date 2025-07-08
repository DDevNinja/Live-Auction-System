from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from auction.views import AuctionViewSet, BidViewSet, WalletViewSet

router = routers.DefaultRouter()
router.register(r'auctions', AuctionViewSet)
router.register(r'bids', BidViewSet)
router.register(r'wallets', WalletViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
     path('', include(router.urls)),
    path('api/', include('auction.urls')),
]
