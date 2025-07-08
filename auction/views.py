from rest_framework import viewsets
from .models import Auction, Bid, Wallet
from .serializers import AuctionSerializer, BidSerializer, WalletSerializer
from django.http import JsonResponse

# Test view
def test_view(request):
    return JsonResponse({'message': 'Auction app is working fine!'})

# ViewSets
class AuctionViewSet(viewsets.ModelViewSet):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer

class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer

class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
