from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, StreamingHttpResponse
from django.template.loader import render_to_string

from .forms import ReviewsForm, PhotoForm, FileFieldForm
from .models import Photo, Review, VideoReport, Product
from .services import open_video_file

from django.core.mail import send_mail
from django.conf import settings

from django.views.generic.edit import FormView


def index(request):
    if request.method == 'POST':
        data = {
        'name': request.POST['name'],
        'tel': request.POST['tel'],
        'message':request.POST['message'],
        'email': request.POST['email']
        }
        send_mail('PetDelivery', render_to_string('Cargo/send_email.html', data), 'settings.EMAIL_HOST_USER', ['petdelivery.moscow@gmail.com'], fail_silently=False, html_message=render_to_string('Cargo/send_email.html', data))      
    return render(request, 'Cargo/index.html')


class AddReviews(FormView):
    template_name = 'Cargo/add_reviews.html'
    form_class = ReviewsForm
    model = Review
    success_url = '/'
    success_message = 'Успешно отправлено'
    
    def get(self, request):
      form = self.form_class() 
        
      return render(request, self.template_name, {'form': form})
    
    def post(self, request):
      form = self.form_class(request.POST)
      
      if form.is_valid():
          id = form.save().pk
          name = Review.objects.get(pk=id)
          files = request.FILES.getlist('file')
          if files:
            for f in files:
              fl = Photo(name=name, photo = f)
              fl.save()
      else:
        return self.form_invalid(),
      
      return HttpResponse('''
                          <body style='margin:0'>
                          <div class='forms_container' style='height:100vh;max-width:unset;
                          background: -webkit-linear-gradient(90deg, #6340a2,#17dba3,#0b7373);
                          background: linear-gradient(90deg, #6340a2,#17dba3,#0b7373);
                          border-radius:unset;
                          position:relative'>
                        
                          <div style='display: flex;
                          position:absolute;
                          justify-content: center;
                          align-items: center;
                          flex-direction: column;
                          width: 50%;
                          height: 50vh;
                          font-size:17px;
                          margin: 25vh 25%;
                          color: azure;
                          background: rgba(255, 255, 255, 0.192);
                          backdrop-filter: blur(10px);
                          border-radius: 15px;'>
                          <span style="margin-bottom:30px;">Принято! Ваш отзыв будет опубликован в ближайшее время</span>
                          <a style=" cursor: pointer;
                          width: 30%;
                          height: 3rem;
                          background-color: #e9e921;
                          color: #093b46;                        
                          font-family: 'Montserrat', sans-serif;
                          font-weight: 800;
                          font-size: 15px;
                          border: none;
                          border-radius: 10px;
                          text-decoration:none" href="/"><span style='position:absolute;padding:1rem 9.3%'>Главная</span></a></div></div></body>''')
 
 


def reports(request):
  video_list = VideoReport.objects.all()
  return render(request, 'Cargo/reports.html', {'video_list': video_list})
  

 
def get_video(request, pk: int):
  _video = get_object_or_404(VideoReport, id=pk)
  return render(request, 'Cargo/video_report.html', {'video': _video})


def get_streaming_video(request, pk: int):
  
  file, status_code, content_length, content_range = open_video_file(request, pk)
  response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')
  
  response['Accept-Ranges'] = 'bytes'
  response['Content-Length'] = str(content_length)
  response['Cache-Control'] = 'no-cache'
  response['Content-Range'] = content_range
  
  return response 
 
  
def reviews(request):
  review = Review.objects.filter(moderation=True)
  photos = Photo.objects.all()
  return render(request, 'Cargo/reviews.html', {'review': review, 'photos': photos})

def services(request):
  products = Product.objects.all()
  return render(request, 'Cargo/products_and_services.html', {'products': products}) 