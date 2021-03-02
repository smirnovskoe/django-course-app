from django.contrib import admin
from django.urls import path, include

from courses.views import LandingPageView, SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', LandingPageView.as_view(), name='landing-page'),
    path('courses/', include('courses.urls', namespace='courses')),
]
