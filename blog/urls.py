from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r"^post/(\d+)/$", views.post, name="post"),
    url(r"^postsby/(\d+)/$", views.user_post_list, name="user_post_list"),
    url(r"^contributors/$", views.user_list, name="user_list"),
]
