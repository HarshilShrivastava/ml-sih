from django.shortcuts import render,get_object_or_404
from .serializers import ResumeSerializer,ResumegetSerializer,TextSerializer
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
from django.conf import settings


import nltk
import pandas as pd
import spacy
import os
#from django.conf.settings import PROJECT_ROOT

#ile_ = open(os.path.join(PROJECT_ROOT, 'skills.csv'))

# load pre-trained model
nlp = spacy.load('en_core_web_sm')
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
            data = ResumeParser("/home/sihml/ml-sih/sih_ml"+(obj.Resume.url)).get_extracted_data()
            #data=obj.Resume.url
            return Response(data)
        else:
            return Response(serializer.errors)

@api_view(['POST', ])
@permission_classes((AllowAny, ))
def analysis_api(request):
    context={}
    data={}
    context['sucess']=True
    context['status']=200
    context['response']="sucessfull"
    if request.method == 'POST':
        serializer = ResumegetSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data['username']
            obj=get_object_or_404(Result,username=name)
            data = ResumeParser("/home/sihml/ml-sih/sih_ml"+(obj.Resume.url)).get_extracted_data()
            #data=obj.Resume.url
            return Response(data['skills'])
        else:
            return Response(serializer.errors)




@api_view(['POST', ])
@permission_classes((AllowAny, ))
def get_skills(request):
    context={}
    data={}
    context['sucess']=True
    context['status']=200
    context['response']="sucessfull"
    if request.method == 'POST':
        serializer = TextSerializer(data=request.data)
        if serializer.is_valid():
            resume_text=serializer.validated_data['Txt']
            nlp_text = nlp(resume_text)
            noun_chunks = nlp_text.noun_chunks
            tokens = [token.text for token in nlp_text if not token.is_stop]
            raw_data = open("skills.csv", 'rb').read()

            df = pd.read_csv("skills.csv")
            a=df.skill_name
            skills = list(a)
            skillset = []
            for token in tokens:
                if token.lower() in skills:
                    skillset.append(token)
            for token in noun_chunks:
                token = token.text.lower().strip()
                if token in skills:
                    skillset.append(token)
            return Response(skillset)
                    
        else:
            return Response(serializer.errors)

