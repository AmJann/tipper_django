from django.urls import path
from .views import *

urlpatterns =[
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('registration/', Registration.as_view(), name='registration'),
    path('post-list/', PostList.as_view(), name='post_list'),
    path('post-detail/<uuid:id>/', PostDetail.as_view(), name='post_detail'),
    path('comment-list/', CommentList.as_view(), name='comment_list'),
    path('comment-detail/<uuid:id>/', CommentDetail.as_view(), name='comment_detail'),
]