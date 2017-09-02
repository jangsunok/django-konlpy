from rest_framework import serializers

from CauChat.models import Chat, Key


class KeySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    label = serializers.CharField(max_length=100)
    priority = serializers.IntegerField()

    def create(self, validated_data):
        return Key.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.label = validated_data.get('label', instance.label)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.save()
        return instance


class ChatSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    content = serializers.CharField()

    def create(self, validated_data):
        return Chat.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
