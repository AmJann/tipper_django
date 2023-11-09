from django.urls import path
from .views import *

urlpatterns =[
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('registration/', Registration.as_view(), name='registration'),
    path('list/', Post.as_view(), name='post_list'),
    path('detail/', Post.as_view(), name='post_detail'),
]