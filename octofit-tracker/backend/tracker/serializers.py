from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Activity


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Activity
        fields = ["id", "user", "activity_type", "duration_minutes", "distance_km", "date"]

    def get_id(self, obj):
        return str(obj.pk)
