from django.http import HttpResponse
from django.template import loader

def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def info(request):
  template = loader.get_template('info.html')
  return HttpResponse(template.render())

def products(request):
  template = loader.get_template('products.html')
  
  return HttpResponse(template.render())
def About_Us(request):
  template = loader.get_template('about.html')
  
  return HttpResponse(template.render())

def contact_Us(request):
  template = loader.get_template('contact.html')
  
  return HttpResponse(template.render())

def gallery(request):
  template = loader.get_template('gallery.html')
  
  return HttpResponse(template.render())