from django.contrib import admin
from django.urls import path, include

from courses.views import LandingPageView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls', )),
    path('accnts/', include('accnts.urls', namespace='accnts')),

    path('', LandingPageView.as_view(), name='landing-page'),
    path('courses/', include('courses.urls', namespace='courses')),
]
