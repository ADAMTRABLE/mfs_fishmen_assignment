from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Arrival,Payment

from rest_framework import generics,status
from rest_framework.response import Response
from . import serializers

# Create your views here.

class ArrivalCreateListView(generics.GenericAPIView):
    serializer_class = serializers.ArrivalCreation

    queryset = Arrival.objects.all()
    def get(self,request):
        arrive = Arrival.objects.all()

        serializer = self.serializer_class(instance=arrive, many=True)

        return Response(data=serializer.data ,status=status.HTTP_200_OK)
    
    def post(self,request):
        data = request.data
        serializer =self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    



class ArrivalDetailView(generics.GenericAPIView):
     
     serializer_class = serializers.ArrivalDetails
     
     def get(self,request,arrival_id):
         room = get_object_or_404(Arrival,pk=arrival_id)
         serializer = self.serializer_class(instance = room)

         return Response(data=serializer.data, status=status.HTTP_200_OK)
     
     def put(self,request,arrival_id):
        room = get_object_or_404(Arrival,pk=arrival_id)
        serializer = self.serializer_class(room,data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        
     def delete(self,request,arrival_id):
         room = get_object_or_404(Arrival,pk=arrival_id)
         serializer = self.serializer_class(instance = room)

         if serializer:
             room.delete()

             return Response({'message':'finally deleted'}, status=status.HTTP_204_NO_CONTENT)
         
class PaymentCreateListView(generics.GenericAPIView):
    serializer_class = serializers.PaymentSerializer

    def get_queryset(self):
        return Payment.objects.all()

    def get(self, request,arrival_id):
        payments = self.get_queryset()
        serializer = self.serializer_class(instance=payments, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request,arrival_id):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)