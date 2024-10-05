from rest_framework import serializers

from Inventory.models import Inventory

class InventorySerializer(serializers.ModelSerializer):
    
    review_user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        
        model = Inventory
        fields = '__all__'