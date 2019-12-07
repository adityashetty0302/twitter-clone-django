from django.urls import path
from . import views

app_name = 'tweets'

urlpatterns = [
    path('new/', views.CreateTweet.as_view(), name='new'),
    path('my-tweets/<username>', views.MyTweets.as_view(), name='my-tweets'),
    path('delete/<int:pk>', views.delete_tweet, name='delete'),
    path('delete-success/', views.DeleteSuccess.as_view(), name='delete-success'),
    path('home-tweets/<int:pk>', views.HomeTweets.as_view(), name='home-tweets'),
]
