# blog_app/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comment
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(
        required=True, validators=[
            UniqueValidator(queryset=User.objects.all())])
    
    class Meta:
        model = User
        fields = ['id','email', 'username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request', None)
        if request and not request.user.is_anonymous:
            validated_data['author'] = request.user
        return super().create(validated_data)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)  # Automatically set, so read_only
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())  # Must be provided in request

    class Meta:
        model = Comment
        fields = '__all__'
