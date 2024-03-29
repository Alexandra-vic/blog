from rest_framework import serializers

from django.contrib.auth import get_user_model

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id', 
            'title', 
            'body', 
            'date', 
            'updated_on', 
            'author',
        )
        

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = (
            'id', 
            'username',
        )        
