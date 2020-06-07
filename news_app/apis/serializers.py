from rest_framework import serializers
from news_app.models import Category, News
from account.apis.serializers import UserSerializer


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "id", "title"


class NewsSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer(read_only=True, many=True)
    category_ids = serializers.PrimaryKeyRelatedField(
        write_only =True,many=True, queryset=Category.objects.all(),source="category"
    )
    author = UserSerializer(read_only=True)

    class Meta:
        model = News
        fields = "id", "title", "author", "content", "category", "category_ids", "created_at"