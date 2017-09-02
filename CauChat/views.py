

from rest_framework import routers, serializers, viewsets, status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from CauChat.chat_parser import get_best_key
from CauChat.models import Chat, Key
from CauChat.serializers import ChatSerializer, KeySerializer


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def get_reply(request):
    if request.method == 'GET':
        chats = Chat.objects.all()
        serializer = ChatSerializer(chats, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            content = serializer.data['content']
            print("content is ", content)
            get_best_key(content)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def key_list(request):
    if request.method == 'GET':
        keys = Key.objects.all()
        serializer = KeySerializer(keys, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = KeySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






