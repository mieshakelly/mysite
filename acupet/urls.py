from django.urls import path
from . import views
from .views import articles_view

app_name = 'acupet'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('1/', articles_view, name = 'myArticles'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('https://www.google.com/maps/search/?api=1&query=/', views.DetailView.as_view(), name='google'),
]
