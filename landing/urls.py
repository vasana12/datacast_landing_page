from django.urls import path
from landing.views import *
from django.contrib.auth import views as auth_views
from django.template.defaultfilters import slugify
app_name = 'landing'
urlpatterns = [
    path('',main_page,name='index'),

    #class_based views
    path('boards_list/',BoardListView.as_view(),name='boards_list'),
    path('reivew_request_list/', BoardListView.as_view(), name='boards_list'),

    path('boards_detail/<int:pk>/', BoardDetailView.as_view(), name='boards_detail'),

    ###request 요청시 추가

    path('review_search_task_add', Review_search_taskCreateView.as_view(), name='review_search_task_add'),
    path('analysis_add',BoardCreateView.as_view(), name='analysis_add'),
    path('datacast_request_create', datacast_request_create, name='datacast_request_create'),
    path('start', start, name='start'),
    path('almaden_datahero', almaden_datahero, name='almaden_datahero'),
    path('blog',blog,name='blog'),
    # path('feature',feature,name='feature'),
    path('pricing', pricing, name='pricing'),
    path('blog-details', blog_details, name='blog_details'),
    path('contact', contact, name='contact'),
]