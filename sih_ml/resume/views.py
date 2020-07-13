from django.shortcuts import render,get_object_or_404
from .serializers import ResumeSerializer
from rest_framework.response import Response
from .models import Result
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.decorators import (
    api_view,
    permission_classes,
)
import nltk
#nltk.download('stopwords')
from pyresparser import ResumeParser

@api_view(['POST', ])
@permission_classes((AllowAny, ))
def analysis(request):
    context={}
    data={}
    context['sucess']=True
    context['status']=200
    context['response']="sucessfull"
    if request.method == 'POST':
        serializer = ResumeSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data['username']
            serializer.save()
            
            obj=get_object_or_404(Result,username=name)
            data = ResumeParser(obj.Resume.url).get_extracted_data()
            #data=obj.Resume.url
            return Response(data)
        else:            
            return Response(serializer.errors)





# Create your views here.
