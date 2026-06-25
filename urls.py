from django.urls import path
from . import views 
# from .views import movies_by_category 

urlpatterns = [
    path('home/', views.home, name='home'),
    path('movies/<int:movie_id>/', views.movie, name='movie'),
    path('payment/',views.payment_page, name='payment_page'), # صفحة الدفع

# path('category/<str:category_name>/', movies_by_category, name='movies_by_category'),
    # urls.py

]