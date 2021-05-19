from django.contrib.auth.views import LogoutView
from django.urls import path

from news.views import (NewsCreateView, NewsDetailView,
                        NewsListView, NewsStatisticsView, LoginView)

urlpatterns = [
    path('', NewsListView.as_view(), name='all_news'),
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('create/', NewsCreateView.as_view(), name='create_news'),
    path('statistics/', NewsStatisticsView.as_view(), name='news_statistics'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
