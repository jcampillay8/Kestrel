
# backend/core/urls.py
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include(('apps.authentication.urls',
         'authentication'), namespace='authentication')),
    path('user/', include(('apps.user.urls', 'user'), namespace='user')),
    path('skill_builder/', include('apps.skill_builder.urls')),
    path('skill_practice/', include('apps.skill_practice.urls')),
]
