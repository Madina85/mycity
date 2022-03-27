from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ProposalListSerialiser
from .models import Proposal

class ProposalListAPView(APIView):
    def get(self, request, *args, **kwargs):
        proposals = Proposal.objects.all()
        proposals_json = ProposalListSerialiser(proposals, many=True)
        
        return Response(data=proposals_json.data)


