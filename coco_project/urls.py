from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('pages.urls')),
    path('users/', include('users.urls')),
    path('users/',include('allauth.urls')),
    path('problems/', include('problems.urls')),
    path('comments/', include('comments.urls')),
    path('blogs/', include('blog.urls')),
    path('news/', include('news.urls')),
    path('admin/', admin.site.urls),
    path('martor/', include('martor.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
