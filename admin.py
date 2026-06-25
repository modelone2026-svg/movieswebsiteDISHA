from django.contrib import admin

# Register your models here.

from .models import Movie, Episode

class EpisodeInline(admin.TabularInline):
    model = Episode
    extra = 1  # عدد الحقول الإضافية لعرضها

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    inlines = [EpisodeInline]  # عرض الحلقات داخل صفحة الفيلم
    list_display = ['title', 'category', 'release_date', 'is_vip']
    search_fields = ['title', 'category']