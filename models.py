from django.db import models

# Create your models here.

class Movie_kids (models.Model):
    CATEGORY_CHOICES = [
        ('كوميدي', 'كوميدي'),
        ('دراما', 'دراما'),
        ('اكشن', 'اكشن'),
        ('جريمة', 'جريمة'),
        ('رومانسي', 'رومانسي'),
        ('خيال علمي', 'خيال علمي'),
        ('تشويق', 'تشويق'),
        # يمكنك إضافة المزيد من التصنيفات هنا
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100 , choices=CATEGORY_CHOICES, default='كوميدي')
    release_date = models.DateField()
    rating = models.FloatField()
    image = models.ImageField(upload_to='movies/')
    video_file = models.FileField(upload_to='movies/videos/', null=True, blank=True)
    video_url = models.URLField(max_length=500, blank=True)
    is_vip = models.BooleanField(default=False)
    duration = models.PositiveIntegerField(help_text="المدة بالدقائق", default=0)
    
    QUALITY_CHOICES = [
        ('HD', 'جودة عالية'),
        ('FHD', 'جودة فائقة'),
        ('4K', 'جودة 4K'),
    ]
    quality = models.CharField(max_length=3, choices=QUALITY_CHOICES, default='HD')
    subtitles = models.FileField(upload_to='movies/subtitles/', blank=True)
    
    def __str__(self):
        return self.title


class Episode_kids (models.Model):
    movie = models.ForeignKey(Movie_kids, on_delete=models.CASCADE, related_name='episodes')
    episode_number = models.PositiveIntegerField()
    title = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='series/episodes/')
    video_url = models.URLField(max_length=500, blank=True)
    release_date = models.DateField()
    
    def __str__(self):
        return f"{self.movie.title} - الحلقة {self.episode_number}"

