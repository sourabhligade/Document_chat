# document_processing/models.py

from django.db import models

class Document(models.Model):
    file = models.FileField(upload_to='documents/')
    asset_id = models.CharField(max_length=255, unique=True)

class Embedding(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    embedding_vector = models.JSONField()  # Store the embedding vector as JSON
