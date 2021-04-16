from rest_framework import viewsets

from channels.models import Channel, Item
from channels.serializers import ChannelSerializer, ItemSerializer

class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer

    def get_queryset(self):
        return Item.objects.filter(
            channel=self.kwargs["channel_pk"])