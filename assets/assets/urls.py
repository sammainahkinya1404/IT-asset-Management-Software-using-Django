

from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.views.generic import RedirectView
# from django.contrib.auth.decorators import login_required






urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('assetApp.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL)
