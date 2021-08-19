from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SolutionPage
from .serializers import SolutionPageSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView


class SolutionDetail(APIView):
    def get_object(self, pk):
        print(pk)
        try:
            return SolutionPage.objects.get(pk=pk)
        except SolutionPage.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        solution = self.get_object(pk)
        serializer = SolutionPageSerializer(solution, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
