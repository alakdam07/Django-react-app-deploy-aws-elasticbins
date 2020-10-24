from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ArticleSerializer
from .models import Article


@api_view(['GET'])
def apiOverview(request):
    api_urls ={
        'List': '/article-list/',
        'Detail View': '/article-detail/<str:pk>/',
        'Create':'/article-create/',
        'Update': '/article-update/<str:pk>/',
        'Delete': '/article-delete/<str:pk>/'
    }
    return Response(api_urls)


@api_view(['GET'])
def articleList(request):
	articles = Article.objects.all().order_by('date')
	serializer = ArticleSerializer(articles, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def articleDetail(request, pk):
	articles = Article.objects.get(id=pk)
	serializer = ArticleSerializer(articles, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def articleCreate(request):
	serializer = ArticleSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def articleUpdate(request, pk):
	article = Article.objects.get(id=pk)
	serializer = ArticleSerializer(instance=article, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)



@api_view(['DELETE'])
def articleDelete(request, pk):
	article = Article.objects.get(id=pk)
	article.delete()

	return Response("Item deleted")

