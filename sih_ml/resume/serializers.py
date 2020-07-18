from rest_framework import serializers
from .models import Result,Text
class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Result
        fields="__all__" 
    # intialize fields 
class ResumegetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Result
        fields=['username']

class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model=Text
        fields=['Txt']

