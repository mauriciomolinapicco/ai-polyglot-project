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
        user_message = request.data.get("message", "")
        if not user_message:
            return Response({"error":"Message is required"}, status=status.HTTP_400_BAD_REQUEST)
        openai.api_key = os.getenv("OPENAI_API_KEY")
        # try:
        #     response = openai.ChatCompletion.create(
        #         model="gpt-3.5-turbo",
        #         messages=[{"role": "user", "content": user_message}],
        #     )
        #     return Response({"response": response.choices[0].messsage["content"]}, status=status.HTTP_200_OK)
        # except Exception as e:
        #     return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"response":"La brisa acaricia el amanecer mientras las olas susurran secretos antiguos al mundo. Un pájaro solitario cruza el cielo, dibujando esperanza en su vuelo. Cada instante es un tesoro oculto, una promesa de cambio. El horizonte arde en colores vivos, recordándonos que la vida es un lienzo esperando ser pintado."}, status=status.HTTP_200_OK)