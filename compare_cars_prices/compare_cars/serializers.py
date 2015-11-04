from rest_framework import serializers

from compare_cars.models import CarMakeDetails




class CompareCarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CarMakeDetails
        fields = ('id', 'website_name', 'city', 'makes', 'car_model','price','model_year','car_title','car_href','car_image','car_color','created')
        