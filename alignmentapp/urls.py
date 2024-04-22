from django.urls import path
from alignmentapp import views 


urlpatterns = [
    path('', views.home, name="Home"), 
    path('capabilities', views.capabilities, name="Capabilities"),
    path('whyalignment', views.whyalignment, name="Why Alignment"),
    path('aboutus', views.aboutus, name="About Us"),
    path('contact', views.contact, name="Contact"),
]