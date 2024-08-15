from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Document
import uuid
from .embeddings import generate_embeddings, store_embeddings

def generate_unique_asset_id():
    return str(uuid.uuid4())  # Generates a unique ID

@api_view(['POST'])
def process_document(request):
    file = request.FILES.get('file')
    if file:
        asset_id = generate_unique_asset_id()
        print(f"Generated asset ID: {asset_id}")
        document = Document.objects.create(file=file, asset_id=asset_id)
        print(f"Document created with ID: {asset_id}")
        
        try:
            # Read content from file
            content = file.read().decode('utf-8')  # Assuming text content; adjust as needed
            print(f"File content read: {content[:100]}...")  # Log only the first 100 characters for brevity
            
            # Generate embeddings
            embeddings = generate_embeddings(content)
            
            # Store embeddings
            store_embeddings(asset_id, embeddings)
            
            return Response({'asset_id': asset_id}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(f"Error processing document: {e}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return Response({'error': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)

def upload_page(request):
    return render(request, 'upload.html')
