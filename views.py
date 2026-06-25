from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.

from .models import Movie



def home(request):
    # ... الكود الخاص بالدالة home ...
    comedy_movies = Movie.objects.filter(category='كوميدي')
    drama_movies = Movie.objects.filter(category='دراما')
    action_movies = Movie.objects.filter(category='اكشن')
    crime_movies = Movie.objects.filter(category='جريمة')
    romance_movies = Movie.objects.filter(category='رومانسي')
    sci_fi_movies = Movie.objects.filter(category='خيال علمي')
    thriller_movies = Movie.objects.filter(category='تشويق')

    context = {
        'comedy_movies': comedy_movies,
        'drama_movies': drama_movies,
        'action_movies': action_movies,
        'crime_movies': crime_movies,
        'romance_movies': romance_movies,
        'sci_fi_movies': sci_fi_movies,
        'thriller_movies': thriller_movies,
    }
    return render(request, 'home4.html', context)
def movie(request, movie_id):
    # جلب بيانات الفيلم باستخدام get_object_or_404
    movie = get_object_or_404(Movie, id=movie_id)

    # التحقق مما إذا كان الفيلم مخصصاً لـ VIP
    if movie.is_vip:
        # إعادة توجيه المستخدم لصفحة الدفع إذا كان الفيلم خاصاً بـ VIP
        return redirect('payment_page')  # تأكد من أن اسم URL لصفحة الدفع معرف في ملف urls.py
    else:
        # عرض تفاصيل الفيلم إذا لم يكن مخصصاً لـ VIP
        return render(request, 'home5.html', {'movie': movie})
    
def payment_page(request):
    return render(request, 'payment_page.html')


# def movie(request, movie_id):
#     movie = get_object_or_404(Movie, id=movie_id)  # لجلب بيانات الفيلم
#     return render(request, 'home2.html', {'movie': movie})


# def home(request):
#     movies = Movie.objects.all()
#     return render(request, 'home4.html', {'movies': movies})

# def movies_by_category(request, category_name):
#     movies = Movie.objects.filter(category=category_name)  # تصفية حسب التصنيف




# def home(request):
#     categories = ['أكشن', 'دراما', 'كوميديا', 'رعب']  # أو استخرجها من قاعدة البيانات
#     movies = Movie.objects.all()
#     return render(request, 'home3.html', {'categories': categories, 'movies': movies})
