from django.urls import path
from . import views

urlpatterns = [
    path('calculator/', views.EnergyCalculatorView.as_view(), name='energy-calculator'),
    path('consumers/', views.CreateConsumerView.as_view(), name='create-consumer'),
    path('consumers/list/', views.ListConsumerView.as_view(), name='list-consumers'),
    path('discount-rules/', views.DiscountRuleListView.as_view(), name='discount-rules'),  # Listagem de regras de descontos
    path('consumers/update/<int:pk>/', views.UpdateConsumerView.as_view(), name='update-consumer'),  # Atualização de consumidor
    path('consumers/delete/<int:pk>/', views.DeleteConsumerView.as_view(), name='delete-consumer'),  # Exclusão de consumidor
]
