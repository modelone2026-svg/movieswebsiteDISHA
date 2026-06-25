from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.

from .models import Movie_kids,Episode_kids

# def home_kids(request):
#     movies_kids  = Movie_kids.objects.all()
#     return render(request, 'home3_kids.html', {'movies': movies_kids})

def home_kids(request):
    # ... الكود الخاص بالدالة home ...
    comedy_movies = Movie_kids.objects.filter(category='كوميدي')
    drama_movies = Movie_kids.objects.filter(category='دراما')
    action_movies = Movie_kids.objects.filter(category='اكشن')
    crime_movies = Movie_kids.objects.filter(category='جريمة')
    romance_movies = Movie_kids.objects.filter(category='رومانسي')
    sci_fi_movies = Movie_kids.objects.filter(category='خيال علمي')
    thriller_movies = Movie_kids.objects.filter(category='تشويق')

    context = {
        'comedy_movies': comedy_movies,
        'drama_movies': drama_movies,
        'action_movies': action_movies,
        'crime_movies': crime_movies,
        'romance_movies': romance_movies,
        'sci_fi_movies': sci_fi_movies,
        'thriller_movies': thriller_movies,
    }
    return render(request, 'home4_kids.html', context)

def movie_kids(request, movie_kids_id):  # تأكد من تطابق الاسم مع الـ URL
    movie_kids = get_object_or_404(Movie_kids, id=movie_kids_id)
    return render(request, 'home5_kids.html', {'movie': movie_kids})


# def movies_by_category(request, category_name):
#     movies = Movie.objects.filter(category=category_name)  # تصفية حسب التصنيف


# def movie_kids(request, movie_kids_id):
#     movie_kids  = get_object_or_404(Movie_kids, id=movie_kids_id)  # لجلب بيانات الفيلم
#     return render(request, 'home2_kids.html', {'movie': movie_kids})

