from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
import whisper

model = whisper.load_model("base")

class TranscriberView(APIView):
    parser_class = [FileUploadParser]

    def post(self, request, *args, **kwargs):
        video = request.FILES['file']
        with open(video.name, 'wb') as f:
            for chunk in video.chunks():
                f.write(chunk)

        result = model.transcribe(video.name)
        return Response({"captions": result["segments"]})