from rest_framework.serializers import ModelSerializer
from main import models

class CategorySerializer(ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class PostSerializer(ModelSerializer):
    class Meta:
        model = models.Post
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'
        