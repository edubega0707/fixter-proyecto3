
from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from accounts import urls as accounts_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(accounts_urls, namespace='accounts')),
    url(
        regex=r'^media/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root': settings.MEDIA_ROOT}
    )
]

