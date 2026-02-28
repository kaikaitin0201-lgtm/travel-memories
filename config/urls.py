from django.contrib import admin
from django.urls import path, include  # ← include を追加
from triplog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.map_view, name='map'),
    path('pref/<str:pref_name>/', views.detail_view, name='detail'),
    
    # ↓ 追加：Djangoが元々持っているログイン機能のURLをすべて読み込む
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)