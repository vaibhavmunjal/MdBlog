from django.urls import path
from .views import (Home,
					NewPost,
					PostDetail,
					PostUpdate,
                    post_delete)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', Home.as_view(), name='blog'),
    path('new', NewPost.as_view(), name='create'),
    path('delete', post_delete, name='post_delete'),
    path('post/<slug:slug>', PostDetail.as_view(), name='post'),
    path('post/update/<slug:slug>', PostUpdate.as_view(), name='post_update'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)