from django.urls import path
from .views import process_document, upload_page
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('process/', process_document, name='process_document'),
    path('upload/', upload_page, name='upload_page'),
]

# Serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
