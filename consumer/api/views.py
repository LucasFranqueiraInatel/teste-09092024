from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Consumer
from .serializers import ConsumerSerializer, ConsumerCreateUpdateSerializer
from calculator import calculator as calculate_energy_savings
from ..models import DiscountRule
from .serializers import DiscountRuleSerializer

# View da API para a calculadora de economia de energia
class EnergyCalculatorView(APIView):
    def post(self, request):
        consumptions = request.data.get('consumptions')
        tariff_value = request.data.get('tariff_value')
        tariff_type = request.data.get('tariff_type')

        if not consumptions or not tariff_value or not tariff_type:
            return Response({"error": "Todos os campos são obrigatórios"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            result = calculate_energy_savings(consumptions, tariff_value, tariff_type)
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class CreateConsumerView(generics.CreateAPIView):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerCreateUpdateSerializer

class ListConsumerView(generics.ListAPIView):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['discount_rule__consumer_type', 'consumption'] 

class DiscountRuleListView(APIView):
    def get(self, request):
        rules = DiscountRule.objects.all()
        serializer = DiscountRuleSerializer(rules, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UpdateConsumerView(generics.UpdateAPIView):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerCreateUpdateSerializer

class DeleteConsumerView(generics.DestroyAPIView):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerCreateUpdateSerializer