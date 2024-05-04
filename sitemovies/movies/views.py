from django.shortcuts import render

movies = [
     {
         "title": "Movie 1",
         "duration": "120 min",
         "year": 2023,
         "relevance": True
     },
     {
         "title": "Movie 2",
         "duration": "90 min",
         "year": 2021,
         "relevance": True
     },
     {
         "title": "Movie 3",
         "duration": "150 min",
         "year": 2024,
         "relevance": False
     }
]

def get_movies(request):
    data = {"movies": movies}
    return render(request, 'movies/movies.html', context=data)