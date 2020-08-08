from django.urls import path

from news.views import (
    NewsListView,
    # index_view,
    # edit_news,
    # news_detail,
    NewsDetailView,
    # add_news,
    NewsCreateView,
    # delete_news,
    NewsDeleteView,
    add_comment,
    NewsUpdateView,
)


urlpatterns = [
    path('', NewsListView.as_view(), name='index'),
    path('edit/<slug:slug>/', NewsUpdateView.as_view(), name='edit_news'),
    path('news/<slug:slug>/', NewsDetailView.as_view(), name='detail_news'),
    path('add-news/', NewsCreateView.as_view(), name='add_news'),
    path('delete-news/<slug:slug>', NewsDeleteView.as_view(), name='delete_news'),
    path('add-comment/<slug:slug>', add_comment, name='add_comment'),
]
