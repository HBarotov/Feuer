from django.urls import path


from .views import (
    PostListView,
    PostDetailView,
    # PostCreateView,
    # PostUpdateView,
    # PostDeleteView,
    # UserPostListView,
    about_view,
)

app_name = "blog"
urlpatterns = [
    path("", PostListView.as_view(), name="blog_home"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("about/", about_view, name="blog_about"),
]
