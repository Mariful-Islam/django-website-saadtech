from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

        path('', views.home, name='home'),
        path('register/', views.reg, name='reg'),
        path('login/', views.login, name='login'),
        path('service/', views.service, name='service'),
        path('blog/', views.blog, name='blog'),
        path('books/', views.book, name='book'),
        path('profile/user.username/', views.profile, name='profile'),
        path('logout/',views.logout, name = 'logout'),
        url(r'^download/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)