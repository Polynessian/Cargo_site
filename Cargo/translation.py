from modeltranslation.translator import register, TranslationOptions
from .models import Review, VideoReport, Product, Photo


@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('title', 'way', 'content', 'answer')
    
    
@register(VideoReport)
class VideoReportTranslateOptions(TranslationOptions):
    fields = ('title', 'description')
    
@register(Product)
class ProductTranslateOptions(TranslationOptions):
    fields = ('title', 'description')
    


    