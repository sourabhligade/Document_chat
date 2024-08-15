from django.db import models

class Document(models.Model):
    file = models.FileField(upload_to='documents/')
    asset_id = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"Document {self.asset_id}"

class Embedding(models.Model):
    asset_id = models.CharField(max_length=255, default='default_value')  # Set a default value here
    embedding = models.JSONField()  # Use JSONField to store embeddings as JSON

    def __str__(self):
        return f"Embedding for {self.asset_id}"
