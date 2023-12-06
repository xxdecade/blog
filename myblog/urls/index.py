from django.urls import path, include
from myblog.views.index import index

urlpatterns = [
    path("", index, name="index"),
    path("posts/", include("myblog.urls.posts.index")),
    path("comments/", include("myblog.urls.comments.index")),
    path("users/", include("myblog.urls.users.index")),
]