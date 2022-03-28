from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ProposalListSerialiser, \
    ProposalCreateSerializer, ProposalSerializer
from .models import Proposal

class ProposalListAPView(APIView):
    def get(self, request, *args, **kwargs):
        proposals = Proposal.objects.all()
        proposals_json = ProposalListSerialiser(proposals, many=True)
        
        return Response(data=proposals_json.data)


class ProposalCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.POST
        serializer = ProposalCreateSerializer(data=data)
        if serializer.is_valid():
            proposal = serializer.save()
            json_data = ProposalSerializer(instance=proposal)
            return Response(json_data, 201)