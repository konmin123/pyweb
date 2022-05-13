from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import note_created

from blog.models import Note



class NoteListCreateAPIView(APIView):
    def get(self, request: Request):
        # Объект который будет передан в шаблон
        context = {
            'все записи': [note_created(note) for note in Note.objects.all()],
        }
        return Response(context)

    def post(self, request):
        data = request.data
        note = Note(**data)

        note.save(force_insert=True)

        return Response(note_created(note), status=status.HTTP_201_CREATED)


class NoteDetailAPIView(APIView):
    def get(self, request, pk):
        note = get_object_or_404(Note, pk=pk)

        return Response(note_created(note))

    def put(self, request, pk):
        ...

