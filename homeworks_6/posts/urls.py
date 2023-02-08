from django.urls import path
from posts.views import  IndexView,PostUpdateView,PostDetailView, PostCreateView,PostDeleteView,AboutView,ContactView

urlpatterns = [
    path('', IndexView.as_view(), name="main-page"),
    # path('hello/', hello, name="hello"),
    # path('post/', PostView.as_view(), name="post"),
    # 
    # path('time/', time, name="time"),
    # path('goodbye/', goodbye, name="goodbye"),
    path('about/', AboutView.as_view(), name="about-page"),
    path('contacts/', ContactView.as_view(), name="contacts"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/create/", PostCreateView.as_view(), name="post-create"),
    path("post/delete/<int:pk>", PostDeleteView.as_view(), name="post-delete"),
    path("post/update/<int:pk>", PostUpdateView.as_view(), name="post-update"),

]

