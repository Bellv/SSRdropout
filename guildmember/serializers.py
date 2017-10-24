from rest_framework import serializers

from posts.models import Post
from .serializers import PostSerializer

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()

a
f
