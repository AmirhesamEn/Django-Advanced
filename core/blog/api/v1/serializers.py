from accounts.models import Profile
from rest_framework.reverse import reverse
from rest_framework import serializers

from blog.models import Category, Post

# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
#     author = serializers.CharField()
#     status = serializers.BooleanField()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    # content = serializers.ReadOnlyField()
    snippet = serializers.ReadOnlyField(source="get_snippet")
    relative_url = serializers.URLField(source="get_absolute_api_url",
                                        read_only=True)
    absolute_url = serializers.SerializerMethodField(
        method_name="get_abs_url")
    category = serializers.SlugRelatedField(
        many=False, slug_field="name", required=False,
        queryset=Category.objects.all()
    )

    # category = CategorySerializer()
    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "image",
            "title",
            "content",
            "relative_url",
            "absolute_url",
            "snippet",
            "status",
            "category",
            "created_date",
            "updated_date",
            "published_date",
        ]
        read_only_fields = ["author", "content"]

    def get_abs_url(self, obj):
        request = self.context.get("request")
        return reverse("blog:api-v1:post-detail", args=[obj.pk],
                       request=request)
        return request.build_absolute_uri(obj.pk)

    def to_representation(self, instance):
        request = self.context.get("request")
        rep = super().to_representation(instance)
        rep["category"] = CategorySerializer(
            instance.category, context={"request": request}
        ).data
        if request.parser_context.get("kwargs").get("pk"):
            rep.pop("snippet", None)
            rep.pop("absolute_url", None)
            rep.pop("relative_url", None)
        else:
            rep.pop("content", None)

        print(request.__dict__)
        return rep

    def create(self, validated_data):
        validated_data["author"] = Profile.objects.get(
            user__id=self.context.get("request").user.id
        )
        return super().create(validated_data)
