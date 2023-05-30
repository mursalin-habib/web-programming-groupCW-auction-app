from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework import generics, status
from auctions.models import Item, ItemComment
from rest_framework import viewsets
from auctions.api.serializers import ItemSerializer, ItemCommentSerializer
from auctions.filters import ItemApiFilter


class ItemModelViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filterset_class = ItemApiFilter


class ItemCommentModelViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    queryset = ItemComment.objects.all()
    serializer_class = ItemCommentSerializer

    @action(url_path='item/(?P<id>\w+)', detail=False)
    def get_item_comments(self, request, id):
        urls = ItemComment.objects.filter(item_id=id)
        page = self.paginate_queryset(urls)
        if page is not None:
            serializer = ItemCommentSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(urls, many=True)
        return Response(serializer.data)
