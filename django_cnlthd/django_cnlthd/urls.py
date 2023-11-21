from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from home.views import index
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('home.urls') ),
    path('api-auth/', include('rest_framework.urls')),
    path("auth/", include("auth_app.urls"), name="auth_app"),
    path("products/", include("products.urls"), name="products"),
    path("cart/", include('cart.urls'), name='cart')
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()
