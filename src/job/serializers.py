from django.utils import timezone
from rest_framework import serializers

from job.models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        # exclude = ('user', 'company', 'creation_date')

    def create(self, validated_data):
        user = self.context['user']
        validated_data['user'] = user
        validated_data['company'] = user
        validated_data['creation_date'] = timezone.now()
        return super().create(validated_data)
