from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()
    

class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    #Если в througmodel есть два fk на одну и туже таблицу, то для однозначности надо использовать through_fields
    users = models.ManyToManyField(UserModel, through='ThroughModel', blank=True, related_name='articles')


class ThroughModel(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_users')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='user_articles')
    external_url = models.TextField()



    
    
    
    
