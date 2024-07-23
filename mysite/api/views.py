from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BlogPost
from .serializers import BlogPostSerializer

from django.http import JsonResponse
from rest_framework.decorators import api_view

from rest_framework.permissions import IsAuthenticated
from rest_framework import status

import requests
API_KEY = '0eec68b0b8b94b39843da25b37cd2ff4'

#These are some of the instances present in the generic.

# ListAPIView: For read-only endpoints to list a collection of model instances.
# CreateAPIView: For write-only endpoints to create a new model instance.
# RetrieveAPIView: For read-only endpoints to retrieve a single model instance.
# UpdateAPIView: For write-only endpoints to update a model instance.
# DestroyAPIView: For write-only endpoints to delete a model instance.
# ListCreateAPIView: For endpoints that allow listing all instances of a model and creating a new instance.
# RetrieveUpdateAPIView: For endpoints that allow retrieving and updating a model instance.
# RetrieveDestroyAPIView: For endpoints that allow retrieving and deleting a model instance.
# RetrieveUpdateDestroyAPIView: For endpoints that allow retrieving, updating, and deleting a model instance.

#These views are known as class based views.

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    permission_classes = [IsAuthenticated]

    def delete(self,request , *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]


#These views are function based views.

# @api_view(['GET', 'POST'])
# def blog_list(request):
#     if request.method == 'GET':
#         queryset = BlogPost.objects.all()
#         serializer = BlogPostSerializer(queryset, many = True)
#         return JsonResponse(serializer.data, safe = False)
    
#     if request.method == 'POST':
#         serializer = BlogPostSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['GET', 'PUT', 'DELETE'])        
# def blog_detail(request,pk):
#     try:
#         blog = BlogPost.objects.get(pk=pk)
#     except BlogPost.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = BlogPostSerializer(blog)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = BlogPostSerializer(blog, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         blog.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


#This is public API key (NEWS API)

def home(request):
    url = f'https://newsapi.org/v2/top-headlines?country=in&apikey={API_KEY}' 
    Response = requests.get(url)
    data = Response.json()
    articles = data['articles']
    
    context = {
        'articles' : articles
    }

    return render(request, 'home.html',context)