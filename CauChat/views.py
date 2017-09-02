import json

from django.http import JsonResponse
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from CauChat.chat_parser import get_best_key
from CauChat.models import Chat, Key, Reply
from CauChat.serializers import ChatSerializer, KeySerializer, ReplySerializer


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def get_reply(request):
    if request.method == 'GET':
        return Response(status=status.HTTP_200_OK)

    elif request.method == 'POST':
        content = request.data['content']
        print("content is ", content)
        best_key = get_best_key(content)

        if best_key is not None:
            ret = {'id': best_key.pk, 'label': best_key.label, 'priority': best_key.priority}
            reply = Reply.objects.get(key=best_key.pk)
            if reply is not None:
                ret = {'id': best_key.pk, 'label': best_key.label,
                       'priority': best_key.priority, 'content': reply.content}
            return Response(data=ret, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)


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


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def add_reply(request):
    if request.method == 'GET':
        replies = Reply.objects.all()
        serializer = ReplySerializer(replies, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
