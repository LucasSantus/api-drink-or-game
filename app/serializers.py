from rest_framework import serializers

from channels.models import Channel, Item

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = [
            "description",
            "link",
            "title",
        ]

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        exclude = ["channel"]