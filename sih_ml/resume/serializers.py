from rest_framework import serializers
from .models import Result
class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Result
        fields="__all__" 
    # intialize fields 
