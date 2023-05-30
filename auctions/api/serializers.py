from django.contrib.auth.models import User
from rest_framework import serializers
from auctions.models import Item, ItemComment


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class ItemCommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)

    def get_user(self, obj):
        return {
            "id": obj.author.id,
            "username": obj.author.username,
            "image": str("http://127.0.0.1:8000/media/" + str(obj.author.image) if obj.author.image else '')
        }

    class Meta:
        model = ItemComment
        fields = "__all__"
