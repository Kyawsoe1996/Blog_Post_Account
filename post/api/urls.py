from django.urls import  path,include
from django.urls.conf import re_path

from rest_framework.authtoken import views
#router for viewset
from rest_framework.routers import DefaultRouter
from .views import (
    custom_view,
    PostViewSet,
    replyComment,
)

router = DefaultRouter()

app_name = "api"


urlpatterns = [
    # path('',custom_view,name="customer-api"),
    path('posts/<int:postid>/comments/<int:commentid>/reply/',replyComment,name="reply-comment")
]
router.register(r'posts', PostViewSet, basename='post')

urlpatterns += router.urls
