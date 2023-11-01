from rest_framework import serializers

from ads.models import Ad, Comment


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою

class CommentSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    author_image = serializers.ImageField(source='author.image', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    class Meta:
        model = Ad
        fields = '__all__'


class AdDetailSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    author_id = serializers.IntegerField(source='author.id')
    phone = serializers.CharField(source='author.phone', read_only=True)

    # TODO сериалайзер для модели
    class Meta:
        model = Ad
        fields = '__all__'
