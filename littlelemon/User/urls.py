from django.urls import path
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('success/', TemplateView.as_view(template_name='success.html'), name='success'),  
]

