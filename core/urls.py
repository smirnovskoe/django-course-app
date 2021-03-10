from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from courses.views import LandingPageView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls', )),
    path('accnts/', include('accnts.urls', namespace='accnts')),

    path('', LandingPageView.as_view(), name='landing-page'),
    path('courses/', include('courses.urls', namespace='courses')),
    path('lessons/', include('lessons.urls', namespace='lessons')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
