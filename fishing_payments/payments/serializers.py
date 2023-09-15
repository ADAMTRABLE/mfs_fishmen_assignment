from .models import Arrival, Payment
from rest_framework import serializers

class ArrivalCreation(serializers.ModelSerializer):
    fish = serializers.CharField(max_length=30)
    weight = serializers.FloatField()
    cost_per_unit = serializers.FloatField()
    total_amount = serializers.SerializerMethodField()


    class Meta:
        model = Arrival
        fields = '__all__'

    def get_total_amount(self, obj):
        return obj.calculate_total_amount()

class ArrivalDetails(serializers.ModelSerializer):
    fish = serializers.CharField(max_length=30)
    weight = serializers.FloatField()
    cost_per_unit = serializers.FloatField()
    total_amount = serializers.SerializerMethodField()

    class Meta:
        model = Arrival
        fields = '__all__'

    def get_total_amount(self, obj):
        return obj.calculate_total_amount()
    
class PaymentSerializer(serializers.ModelSerializer):
    arrival_id = serializers.IntegerField(source='arrival.id', read_only=True)
    payment_amount = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        fields = '__all__'

    def get_payment_amount(self, obj):
        return obj.calculate_payment()