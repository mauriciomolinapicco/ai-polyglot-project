from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import openai 
import os
from dotenv import load_dotenv

load_dotenv()

class OpenAIView(APIView):
    def post(self, request):
        if not request.data.get("message", ""):
            return Response({"error":"Message is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not request.data.get("language"):
            return Response({"error": "Language is required"}, status=status.HTTP_400_BAD_REQUEST)

        openai.api_key = os.getenv("OPENAI_API_KEY")

        messages = [
           {
               "role":"system",
               "content":"Translate the content after the ## in the language that will be given before the ##" 
           },
           {
               "role":"user",
               "content":str(request.data.get("language","") + "##" + request.data.get("message"))
           }
        ]
       
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
            )
            return Response({"response": response.choices[0].messsage["content"]}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        # if request.data.get("language","") == 'French':
        #     return Response({"response":"j'adore le chocolat et la glace."}, status=status.HTTP_200_OK)
        # elif request.data.get("language", "") == "Portuguese":
        #     return Response({"response":"Eu adoro chocolate e sorvete"}, status=status.HTTP_200_OK)
        # else:
        #     return Response({"response":"私はチョコレートとアイスクリームが大好きです"}, status=status.HTTP_200_OK)