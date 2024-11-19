from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "author",
            "title",
            "body",
            "created",
            "slug",
        )
        model = Post