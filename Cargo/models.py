from django.db import models
from django.core.validators import FileExtensionValidator


class Review (models.Model):
    
    title = models.CharField(("user"), max_length=50)
    way = models.CharField(("Маршрут"), max_length=50)
    content = models.TextField(("Отзыв"))
    date = models.DateTimeField(("Дата"), auto_now_add=True)
    answer = models.TextField(("Ответ"), blank=True) 
    moderation = models.BooleanField(("Модерация"), default=False)
    
    class Meta:
        verbose_name = ("Отзыв")
        verbose_name_plural = ("Отзывы")

    def __str__(self):
       return self.title


class Photo(models.Model):
    name = models.ForeignKey(Review, related_name='photos', blank=True, null=True, on_delete=models.CASCADE)
    photo = models.FileField(('Фото'), blank=True, null=True, upload_to='cargo_media')
    
    class Meta:
        verbose_name = ("Фото")
        verbose_name_plural = ("Фотографии")
        
   
        
        
class VideoReport(models.Model):
    
    title = models.CharField(('Заголовок'), max_length=100)
    title_image = models.ImageField(('Фото к заголовку'), upload_to='cargo_media', blank=True)
    description = models.TextField(('Описание'), blank=True)
    video = models.FileField(('Видео'), upload_to='video')
    create_at_date = models.DateTimeField(('Дата'), auto_now_add=True, validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    addit_image_1 = models.ImageField('Фото_1 к отчету', blank=True, upload_to='reports_photos')
    addit_image_2 = models.ImageField('Фото_2 к отчету', blank=True, upload_to='reports_photos')
    addit_image_3 = models.ImageField('Фото_3 к отчету', blank=True, upload_to='reports_photos')
    addit_image_4 = models.ImageField('Фото_4 к отчету', blank=True, upload_to='reports_photos')
    
    
    class Meta:
        verbose_name = ('Видеоотчет')
        verbose_name_plural = ('Видеоотчеты')
        
    
    def __str__(self):
        return self.title
    
    
    
class Product(models.Model):
    
    title = models.CharField(("Название"), max_length=100)
    product_image_1 = models.ImageField('Фото_1_к_товару', upload_to='product_photos')
    product_image_2 = models.ImageField('Фото_2_к_товару', blank=True, upload_to='product_photos')
    product_image_3 = models.ImageField('Фото_3_к_товару', blank=True, upload_to='product_photos')
    product_image_4 = models.ImageField('Фото_4_к_товару', blank=True, upload_to='product_photos')
    description = models.TextField(('Описание'), blank=True)
    price = models.IntegerField(("Цена"), blank=True, null=True)
    
    class Meta:
        verbose_name = ("Товар")
        verbose_name_plural = ("Товары") 
        
    def __str__(self):
        return self.title   
    