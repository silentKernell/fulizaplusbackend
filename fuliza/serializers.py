from rest_framework import serializers
from .models import FulizaLead

class FulizaLeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FulizaLead
        fields = '__all__'