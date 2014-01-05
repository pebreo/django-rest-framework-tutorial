from django.shortcuts import render
'''
Rest frameworks provides two wrappers you can use to write
API views:
1. @api_view decorator for working with function based views
2. The APIView class for working with class based views

'''
from .models import Snippet
from .serializers import SnippetSerializer
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import mixins
from rest_framework import generics

class SnippetList(generics.ListCreateAPIView):
    """
    This class the same thing as the following mixins:
        mixins.ListModelMixin, 
        mixins.CreateModelMixin, 
        generics.GenericAPIView
    """
    queryset = Snippet.objects.all()
    serializer = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This class the same thing as a class with the following mixins
        mixins.RetrieveModelMixin, 
        mixins.UpdateModelMixin, 
        mixins.DestroyModelMixin, 
        generics.GenericAPIView
    """
    queryset = Snippet.objects.all()
    serializer = SnippetSerializer


class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
        """
        We'll take a moment to examine exactly what's happening here. 
        We're building our view using GenericAPIView, and 
        adding in ListModelMixin and CreateModelMixin.

        The base class provides the core functionality, 
        and the mixin classes provide the .list() and .create() actions.
        We're then explicitly binding the get and post methods 
        to the appropriate actions. Simple enough stuff so far.
        """

        queryset = Snippet.objects.all()
        serializer_class = SnippetSerializer
 
        def get(self, request, *args, **kwargs):
            # GenericAPIView provides list() method
            return self.list(request, *args, **kwargs)

        def post(self, request, *args, **kwargs):
            return self.create(request, *args, **kwargs)

class SnippetDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
        queryset = Snippet.objects.all()
        serializer_class = SnippetSerializer

        def get(self, request, *args, **kwargs):
            return self.retrieve(request, *args, **kwargs)
        
        def put(self, request, *args, **kwargs):
            return self.update(request, *args, **kwargs)
        
        def delete(self, request, *args, **kwargs):
            return self.destroy(request, *args, **kwargs)



# class SnippetList(APIView):
#     """
#     List all snippets or create a new snippet
#     """
#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)

#     def post(self, request, formate=None):
#         serializer = SnippetSerializer(snippets, many=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class SnippetDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance
#     """

#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except:
#             raise Http404
    
#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
    
#     # Update
#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET'])
# def snippet_list(request):
#     return Response(status.HTTP_200_OK)

# @api_view(['GET'])
# def snippet_detail(request, pk):
#     return Response(status.HTTP_200_OK)


#def snippet_list(request):
#    return HttpResponse('hello list')

#def snippet_detail(request):
#    return HttpResponse('hello world')

