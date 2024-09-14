from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from pages import views as pages_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='home/', permanent=False)),
    path('home/', include('home.urls')),
    path('apartments/',include('apartments.urls')),
    path('reservations/',include('reservations.urls')),
    path('user/',include('user.urls')),
    path('contact/',include('contact.urls')),
    path('about-us/', pages_views.about_us),
    path('blog/', include('blog.urls')),
    path('tinymce/', include('tinymce.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)