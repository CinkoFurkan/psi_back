from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import titles, about, event, announcement, team, member, blog, member_info, blog_detail, email , contact, like_view, sponsor


urlpatterns = [
    path('api/link/', titles, name="titles"),
    path('api/about/', about, name='about'),
    path('api/event/', event, name='event'),
    path('api/announcement/', announcement, name='announcement'),
    path('api/team/', team, name="team"),
    path('api/member/', member, name="member"),
    path('api/member/<int:id>/', member_info, name="member_info"),
    path('api/blog/', blog, name='blog'),
    path('api/blog/<int:id>/', blog_detail, name='blog'),
    path('api/email/', email, name='email'),
    path('api/contact/', contact, name='contact'),
    path('api/like_view/', like_view, name= 'like_view'),
    path('api/sponsor/', sponsor, name='sponsor'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
