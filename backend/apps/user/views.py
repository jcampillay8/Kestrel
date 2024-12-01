# System Utils
from django.utils.translation import gettext_lazy as _

# Installed Utils
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from openai import OpenAI
import os
import environ

# App Utils
from .serializers import UserInfoSerializer

# Configura tu cliente OpenAI
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


class RoadMap_Motivation(APIView):
    def post(self, request):
        # Obtén las respuestas del estudiante desde la solicitud
        try:
            answers = request.data.get('answers', [])

            if not answers or len(answers) < 3:
                return Response(
                    {"error": "Por favor, proporciona respuestas completas a las tres preguntas."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Construye el prompt para OpenAI
            prompt = f"""
            Actúa como un motivador y tutor experto en inglés. Basándote en las siguientes respuestas del estudiante:

            1. ¿Cuál es la razón principal por la que deseas aprender inglés?
            {answers[0]}

            2. ¿Qué esperas lograr en los próximos 6 meses?
            {answers[1]}

            3. Imagina que dominas este idioma. ¿Qué harías primero?
            {answers[2]}

            Responde con un mensaje de motivación seguido de un roadmap semanal de cuatro semanas para aprender inglés, adaptado a estas metas. Sé claro, breve y específico.
            """

            # Llamada a OpenAI
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are an expert tutor and motivator."},
                    {"role": "user", "content": prompt},
                ],
                max_tokens=255
            )

            # Extrae la respuesta generada por OpenAI
            roadmap = response.choices[0].message.content.strip()

            return Response({"roadmap": roadmap}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserInfoView(RetrieveAPIView):
    """
    Get the user's information
    """
    # Serializer for user's info
    serializer_class = UserInfoSerializer

    # Authentication class to authenticate the user by token
    authentication_classes = [TokenAuthentication]

    # Class to verify if the user is authenticated
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """
        Returns the authenticated
        user data
        """
        return self.request.user

    def retrieve(self, request, *args, **kwargs):
        # Get the user's data
        instance = self.get_object()

        # Serialize the data
        serializer = self.get_serializer(instance)

        # Return custom message
        return Response(
            {
                "success": True,
                "content": serializer.data
            },
            status=status.HTTP_200_OK
        )
