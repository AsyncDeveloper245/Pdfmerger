from django.urls import path
from . import views
urlpatterns = [
    path('',views.pdf_merge,name='pdf_merge'),
]
