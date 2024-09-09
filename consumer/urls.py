from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.consumer_list, name='consumer_list'),
    path('create/', views.create_consumer, name='create_consumer'),
    path('import-consumers/', views.import_consumers, name='import_consumers'),
    path('calculator/', views.calculator, name='calculator'),
    path('api/', include('consumer.api.urls')),

]
