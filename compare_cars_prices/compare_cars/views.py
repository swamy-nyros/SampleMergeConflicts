from .models import CarMakeDetails
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import serializers
from .serializers import CompareCarSerializer
# Create your views here.

# class HomeView(TemplateView):
#     template_name='home.html'


# class Get_allMakes(generic.ListView):
#     models=CarMakeDetails
#     template_name = 'compare_cars/makes.html'
#     context_object_name = 'AllMakes'
#     def get_queryset(self):
#         return CarMakeDetails.objects.order_by().values('makes').distinct()


# def make_models(request, car_makes):
#     car_models = CarMakeDetails.objects.filter(makes=car_makes)    
#     return render(request, 'compare_cars/model.html', {'car_models':car_models})

class Get_allMakes(generics.ListCreateAPIView):
    """
    List all boards, or create a new board.
    """
    # queryset_results = CarMakeDetails.objects.order_by().values('makes').distinct()
    queryset = CarMakeDetails.objects.order_by().values('makes').distinct()
    serializer_class = CompareCarSerializer


class Get_allMakesDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset_results = CarMakeDetails.objects.order_by().values('makes')
    queryset = CarMakeDetails.objects.filter(makes='Tata')
    serializer_class = CompareCarSerializer
     
