from django.urls import path
from posts.views import IndexView, AboutView, ContactsView, PostDetailView, PostCreateView, PostDeleteView, \
    PostUpdateView

urlpatterns = [
    path("", IndexView.as_view(), name="main-page"),
    path("about/", AboutView.as_view(), name="about-page"),
    path("contacts/", ContactsView.as_view(), name="contacts-page"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/create/", PostCreateView.as_view(), name="post-create"),
    path("post/delete/<int:pk>", PostDeleteView.as_view(), name="post-delete"),
    path("post/update/<int:pk>", PostUpdateView.as_view(), name="post-update"),
]
