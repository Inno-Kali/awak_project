from django.urls import path
# from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView
from . import views


urlpatterns = [
    path('',views.bloghome,  name='blog-home'),
    path('addblog',views.addblog, name='addblog'),

]
