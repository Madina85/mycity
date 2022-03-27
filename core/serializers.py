from rest_framework import serializers
from .models import Proposal


class ProposalListSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = ['id', 'title']