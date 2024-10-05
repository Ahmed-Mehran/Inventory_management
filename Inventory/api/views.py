from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView

from Inventory.models import Inventory
from .serializers import InventorySerializer

from rest_framework import permissions

from .permissions import AdminOrReadOnly, IsUserOrAdminOnly, IsAuthenticated

from django.core.cache import cache


class InventoryListAV(APIView):
    
    permission_classes = [AdminOrReadOnly] 
    
    # def get(self, request):
        
    #     inventory = Inventory.objects.all()
        
    #     serializer = InventorySerializer(inventory, many=True)
        
    #     return Response(serializer.data)
    
    def get(self, request):
        
    # Try to get data from cache
        inventory_data = cache.get('inventory_data')
        
        if not inventory_data:
            # If cache is empty, fetch data from the database
            inventory = Inventory.objects.all()
            
            serializer = InventorySerializer(inventory, many=True)
            
            inventory_data = serializer.data
            
            # Store the data in cache for future use
            cache.set('inventory_data', inventory_data, timeout=300)  # Cache for 5 minutes (300 seconds)
        
        return Response(inventory_data)

    
    def post(self, request):
        
        user = request.user
        
        current_user = request.user
     
        serializer = InventorySerializer(data=request.data)
        
        if serializer.is_valid():
            
            item_data = serializer.validated_data['item']
            
            if Inventory.objects.filter(item=item_data, review_user=current_user).exists():
                
                return Response({"error": "Item already exists"}, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save(review_user=user)
            
            return Response(serializer.data)
         
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class InventoryDetailsAV(APIView):
    
    permission_classes = [IsUserOrAdminOnly]
    
    # def get(self, request, pk):
        
    #     try:
    #         inventory_item = Inventory.objects.get(pk=pk)
            
    #     except Inventory.DoesNotExist:
    #         return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        
    #     serializer = InventorySerializer(inventory_item)
        
    #     return Response(serializer.data)

## CACHED VERSION OF ABOVE GET REQUEST
    def get(self, request, pk):
        # Create a unique cache key for this inventory item
        cache_key = f'inventory_item_{pk}'
        
        # Try to get the item from the cache
        inventory_item_data = cache.get(cache_key)
        
        if not inventory_item_data:
            # If cache is empty, fetch the item from the database
            try:
                inventory_item = Inventory.objects.get(pk=pk)
                
            except Inventory.DoesNotExist:
                return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
            
            # Serialize the inventory item data
            serializer = InventorySerializer(inventory_item)
            
            inventory_item_data = serializer.data
            
            # Store the serialized data in cache with a timeout (e.g., 10 minutes)
            cache.set(cache_key, inventory_item_data, timeout=600)  # Cache for 10 minutes
        
        # Return the cached or newly fetched data
        return Response(inventory_item_data)

    
    def put(self, request, pk):
        
        inventory_item = Inventory.objects.get(pk=pk)
        
        self.check_object_permissions(request, inventory_item)
        
        serializer = InventorySerializer(inventory_item, data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        
        inventory_item = Inventory.objects.get(pk=pk)
        
        self.check_object_permissions(request, inventory_item)
        
        inventory_item.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
        
        
        
        
        
        
        
    
    


    
    
    
    
        
                
            
            
                
                
        
        
        
   

         
    