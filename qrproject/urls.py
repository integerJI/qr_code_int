from django.contrib import admin
from django.urls import path, include
from qr_code import urls as qr_code_urls
from django.conf import settings
from django.conf.urls.static import static
from qrapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('qr_code/', include(qr_code_urls, namespace='qr_code')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)