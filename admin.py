from django.contrib import admin

# Register your models here.
from .models import Movie_kids, Episode_kids

class EpisodeInline(admin.TabularInline):
    model = Episode_kids
    extra = 1  # عدد الحقول الإضافية لعرضها

@admin.register(Movie_kids)
class MovieAdmin(admin.ModelAdmin):
    inlines = [EpisodeInline]  # عرض الحلقات داخل صفحة الفيلم
    list_display = ['title', 'category', 'release_date', 'is_vip']
    search_fields = ['title', 'category']