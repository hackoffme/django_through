from rest_framework import viewsets

from company import serializers, models

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = models.UserModel.objects.all()
    serializer_class = serializers.UserSerializer