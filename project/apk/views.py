from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from apk.models import WatchList,StreamPlatform
from .serializer import WatchListSerializer,StreamPlatformserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import Http404


# Create your views here.


class StreamPlatformList():
   # List all StreamPlatformList, or create a new StreamPlatformList.
    def get(self,request,format=None):
         stream_list=StreamPlatform.objects.all()
         serilizer=StreamPlatformserializer(stream_list,many=True)
         return Response(serilizer.data)
    
    def post(self,request,format=None):
        serializer=StreamPlatformserializer(data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        




class StreamPlatformDetail():
    def get_object(self, pk):
        try:
            return StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            raise Http404
    def get(self,request,pk,format=None):
        Stream_Platform=self.get_object(pk)
        serializer = StreamPlatformserializer(Stream_Platform)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        Stream_Platform=self.get_object(pk)
        serializer = StreamPlatformserializer(Stream_Platform, data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        Stream_Platform=self.get_object(pk)
        Stream_Platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)














################################### function based views #######################3

# def movie_list(request):
#     movie_list=WatchList.objects.all()
#     serilized=WatchListSerializer(movie_list,many=True)
#     return JsonResponse(serilized.data,safe=False)


# def movie_detail(request,pk):
#     movie=WatchList.objects.get(pk=pk)
#     serialized=WatchListSerializer(movie)
#     return JsonResponse(serialized.data)



# #for getting a stream and post a stream
# @api_view(['GET', 'POST'])
# def stream_list(request,format=None):
#     if request.method == 'GET':
#         stream_list=StreamPlatform.objects.all()
#         serilizer=StreamPlatformserializer(stream_list,many=True)
#         return Response(serilizer.data)
#     elif request.method =='POST':
#         serializer=StreamPlatformserializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        

# @api_view(['GET', 'PUT', 'DELETE'])
# def stream_detail(request,pk,format=None):
#    # Retrieve, update or delete a code snippet.

#     try:
#         Stream_Platform = StreamPlatform.objects.get(pk=pk)
#     except StreamPlatform.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = StreamPlatformserializer(Stream_Platform)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = StreamPlatformserializer(Stream_Platform, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         Stream_Platform.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)