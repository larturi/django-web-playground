from django.contrib import admin
from django.urls import path, include
from pages.urls import pages_patterns

# Para que haga el redirect al login custom y no al del admin
# from django.contrib.auth.decorators import login_required
# admin.autodiscover()
# admin.site.login = login_required(admin.site.login)

urlpatterns = [
    path('', include('core.urls')),
    path('pages/', include(pages_patterns)),
    path('admin/', admin.site.urls),
    # Paths de Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
]
