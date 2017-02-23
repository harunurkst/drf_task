from rest_framework import generics
from contact_directory.models import Contact
from contact_directory.serializers import ContactSerializer


class ContactList(generics.ListCreateAPIView):
    """
        A list of all contact. User can add new contact with this endpoint
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        Contact detail Serializer. User can edit and delete a contact
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
