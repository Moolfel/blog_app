from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, UserSerializer


# User Registration View
class UserRegistrationView(generics.CreateAPIView):
    """
    Handles user registration.
    POST: Creates a new user with the provided data.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        """
        Create a new user instance.
        Validates the input data and creates a new user. Returns a response with the user data if successful.
        Handles validation errors and returns appropriate error messages.
        """
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            # Log error details for debugging
            print(e.detail.get('email'))
            print(username_error[0] if (username_error := e.detail.get('userame')) else None)
            return Response(
                {
                    "error": str((username_error[0] if (username_error := e.detail.get('username')) else None) or (
                email_error[0] if (email_error := e.detail.get('email')) else None))},status=status.HTTP_400_BAD_REQUEST)


# User Login View
class UserLoginView(ObtainAuthToken):
    """
    Handles user login and token generation.
    POST: Authenticates the user and returns an authentication token.
    """
    def post(self, request, *args, **kwargs):
        """
        Handles the login request and returns the authentication token.
        Calls the parent class's post method to handle authentication, then retrieves and returns the token.
        """
        response = super(UserLoginView, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})


# Post Views
class PostCreateView(generics.ListCreateAPIView):
    """
    List and create posts.
    GET: List all posts.
    POST: Create a new post with the provided data.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a specific post.
    GET: Retrieve a post by ID.
    PUT/PATCH: Update a post by ID.
    DELETE: Delete a post by ID.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# Comment Views
class CommentCreateView(generics.ListCreateAPIView):
    """
    List and create comments.
    GET: List all comments.
    POST: Create a new comment with the provided data (requires authentication).
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Set the author of the comment to the currently authenticated user.
        The author is automatically set based on the request user.
        """
        serializer.save(author=self.request.user)


class CommentRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a specific comment.

    GET: Retrieve a comment by ID.
    PUT/PATCH: Update a comment by ID.
    DELETE: Delete a comment by ID.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentListByPostView(generics.ListAPIView):
    """
    List comments associated with a specific post.
    GET: List all comments for the post specified by post_id.
    """
    serializer_class = CommentSerializer

    def get_queryset(self):
        """
        Return a queryset of comments filtered by the post ID.

        The post ID is retrieved from the URL parameters.
        """
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id)
