from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import login, register, logout_user, dashboard, profile, edit_profile
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login, name='login'),
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),   # 👈 Add this
    path('logout/', logout_user, name='logout'),
    path('profile/', profile, name='profile'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)