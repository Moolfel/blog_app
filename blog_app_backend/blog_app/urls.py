# blog_app/urls.py
from django.urls import path
from .views import (
    UserRegistrationView,
    PostCreateView, PostRetrieveView, CommentListByPostView,
    CommentCreateView, CommentRetrieveView, UserLoginView
)


urlpatterns = [
    # Authentication Endpoints
    path('auth/register/', UserRegistrationView.as_view(), name='user-registration'),
    path('auth/login/', UserLoginView.as_view(), name='user-login'),

    # Post Endpoints
    path('posts/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostRetrieveView.as_view(), name='post-retrieve'),

    # Comment Endpoints
    path('comments/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/', CommentRetrieveView.as_view(), name='comment-retrieve'),
    path('posts/<int:post_id>/comments/', CommentListByPostView.as_view(), name='comments-by-post'),

]
