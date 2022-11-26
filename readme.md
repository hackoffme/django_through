создаем записи в таблицах Article и UserModel

```
article = models.Article.objects.create(title='df', description='asdf')

user = models.UserModel.objects.create(username='1234')
```

Добавление отношений через запись. Строчки эквивалентны

```
user.articles.add(article, through_defaults={'external_url':'df'})

article.users.add(user, through_defaults={'external_url':'df'})
```

Сериалзиация post запроса. Создание статьи и связи с пользователями, и добавления поля в throug модель
```
{
    "article_users": [
        {"id": 1,
         "external_url": "asdf"
        },
        {"id": 2,
         "external_url": "hlkj"
        }
    ],
    "title": "123",
    "description": "321"
}
```

```
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
```
