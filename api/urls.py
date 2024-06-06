from django.urls import path, include
from . import views

urlpatterns =[
    path("", views.BlogPostListCreate.as_view(), name="blog"),
    path("<int:pk>/", views.BlogPostDetail.as_view(), name="blog_detail")
]