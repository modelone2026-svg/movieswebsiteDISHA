from django.urls import path
from . import views 
# from .views import movies_by_category 

urlpatterns = [
    path('', views.home_kids, name='home_kids'),  # سيكون المسار النهائي: /kids/
    path('movies/<int:movie_kids_id>/', views.movie_kids, name='movie_kids'), # /kids/movies/1/
]
# path('category/<str:category_name>/', movies_by_category, name='movies_by_category'),
    # urls.py



# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home_kids, name='home_kids'),
#     path('movie/<int:movie_id>/', views.movie_kids, name='movie_kids'),
# ]
