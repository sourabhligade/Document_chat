from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from document_processing.views import upload_page  # Import the view you want to use


def debug_view(request):
    return HttpResponse("Debug view working!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/documents/', include('document_processing.urls')),
    path('api/chat/', include('chat.urls')),
    path('', upload_page, name='home'),  # Route for the base URL
    path('debug/', debug_view),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
