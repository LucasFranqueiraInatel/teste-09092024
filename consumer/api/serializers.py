from rest_framework import serializers
from ..models import Consumer, DiscountRule

class DiscountRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountRule
        fields = ['id', 'consumer_type', 'consumption_range', 'discount_value']

class ConsumerSerializer(serializers.ModelSerializer):
    discount_rule = DiscountRuleSerializer(read_only=True)

    class Meta:
        model = Consumer
        fields = [
            'id', 'name', 'document', 'zip_code', 'city', 'state', 
            'consumption', 'distributor_tax', 'discount_rule'
        ]

class ConsumerCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumer
        fields = [
            'id', 'name', 'document', 'zip_code', 'city', 'state', 
            'consumption', 'distributor_tax', 'discount_rule'
        ]

class CoverageRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountRule
        fields = ['consumption_range', 'cover_value']