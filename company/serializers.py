from rest_framework import serializers
from company import models

class ThroughSerializers(serializers.ModelSerializer):
    article = serializers.ReadOnlyField(source='article.id')
    user = serializers.ReadOnlyField(source='user.id')
    id = serializers.IntegerField()
    
    class Meta:
        model = models.ThroughModel
        fields = ['id', 'article', 'user', 'external_url']


class ArticleSerializer(serializers.ModelSerializer):
    article_users = ThroughSerializers(many=True)
    def create(self, validated_data):
        user = [(models.UserModel.objects.get_or_create(id=item['id'])[0], item['external_url']) for item in validated_data.pop('article_users')]
        ret = models.Article.objects.create(**validated_data)
        [ret.users.add(item[0], through_defaults={'external_url': item[1]}) for item in user]
        return ret
    class Meta:
        model = models.Article
        fields = '__all__'
        
        
class UserSerializer(serializers.ModelSerializer):
    user_articles = ThroughSerializers(many=True)
    class Meta:
        model = models.UserModel
        fields = '__all__'