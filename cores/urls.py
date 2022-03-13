from email.mime import image
from django.urls import path
from cores import views as get_product_views
app_name = "cores"
urlpatterns = [path("",get_product_views.get_product,name="home"),path("about/",get_product_views.about,name="about"),path("contact/",get_product_views.contact,name="contact")]
