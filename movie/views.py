from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieSerializers

def home(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movie/home.html', context)

@api_view(['GET'])
def MovieList(request):
    movies = Movie.objects.all()
    serializer = MovieSerializers(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def MovieCategoryList(request,category):
    movies = Movie.objects.filter(category=category)
    serializer = MovieSerializers(movies, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def MovieCreate(request):
    serializer = MovieSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def MovieUpdate(request, pk):
    movie = Movie.objects.get(id=pk)
    serializer = MovieSerializers(instance=movie, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def MovieDelete(request, pk):
    movie = Movie.objects.get(id=pk)
    movie.delete()
    return redirect('api')
