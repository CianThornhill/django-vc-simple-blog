from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # ' ' refers to where /blogs with no further link initially brings us, i.e by default website/blog brings us to this view 'homepage'
    path('', views.home, name='homepage'),
    path('<slug:post>/', views.post_single, name='post_single'),
]