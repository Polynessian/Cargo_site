from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Review, Photo, VideoReport, Product
from modeltranslation.admin import TranslationAdmin
from django.utils.safestring import mark_safe
# Register your models here.





@admin.register(Review)

class ReviewAdmin(TranslationAdmin):
    list_display = ('title', 'way', 'content', 'date', 'answer', 'moderation')
    list_display_links = ('title', 'way', 'content','answer', 'moderation')


@admin.register(VideoReport)

class VideoReportAdmin(TranslationAdmin):
    list_display = ('title', 'description', 'video', 'get_image')
    list_display_links =('title', 'description', 'video', 'get_image')
    
    def get_image(self, obj):
        return mark_safe(f"<img src='{obj.title_image.url}' width='100', height='75'")
    
    get_image.short_description = 'Фото'

@admin.register(Photo)

class PhotoAdmin(ModelAdmin):
    list_display = ('name', 'get_image')
    list_display_links = ('name', 'get_image')
    
    def get_image(self, obj):
        return mark_safe(f"<img src='{obj.photo.url}' width='100', height='75'")
    
    get_image.short_description = 'Фото'

@admin.register(Product)

class ProductAdmin(TranslationAdmin):
    list_display = ('title', 'description')
    list_display_links =('title', 'description')
