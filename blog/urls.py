from django.urls import path
# from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView
from . import views


urlpatterns = [
    path('',views.bloghome,  name='bloghome'),
    path('addblog',views.addblog, name='addblog'),
    path('<int:blog_id>/',views.detail, name='detail')

]
