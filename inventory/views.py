from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Item
from .serializers import ItemSerializer
from django.core.cache import cache
from rest_framework.decorators import api_view


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        item_id = kwargs.get('pk')
        cached_item = cache.get(item_id)
        if cached_item:
            return Response(cached_item)

        item = self.get_object()
        serializer = self.get_serializer(item)
        cache.set(item_id, serializer.data, timeout=60*15)
        return Response(serializer.data)
    
# @api_view(['POST'])
# def create_item(request):
#     serializer = InventoryItemSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

