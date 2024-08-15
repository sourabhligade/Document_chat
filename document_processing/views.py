from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Document, Embedding
import uuid

def generate_unique_asset_id():
    return str(uuid.uuid4())  # Generates a unique ID

@api_view(['POST'])
def process_document(request):
    file = request.FILES.get('file')
    if file:
        # Generate a unique asset_id
        asset_id = generate_unique_asset_id()
        
        # Create a new Document entry with the unique asset_id
        document = Document.objects.create(file=file, asset_id=asset_id)
        
        # Replace with actual embedding logic
        embedding_vector = [0.1, 0.2, 0.3]
        
        # Create a new Embedding entry associated with the document
        Embedding.objects.create(document=document, embedding_vector=embedding_vector)
        
        # Return the unique asset_id in the response
        return Response({'asset_id': asset_id}, status=status.HTTP_201_CREATED)
    
    return Response({'error': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)

def upload_page(request):
    return render(request, 'upload.html')
