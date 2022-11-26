
from django.urls import path

from company import views

urlpatterns = [
    path('company/', views.ArticleViewSet.as_view({'get': 'list', 'post': 'create'})),
    
]
