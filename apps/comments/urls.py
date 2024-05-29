from django.urls import path

from apps.comments import views


urlpatterns = [
    path('com/', views.CommentListView.as_view(), name='com_list'),
    path('com/create/', views.CommentCreateView.as_view(), name='com_create'),
    path('com/detail/<int:pk>/', views.CommentDetailView.as_view(), name='com_detail'),
    path('com/update/<int:pk>/', views.CommentUpdateView.as_view(), name='com_update'),
    path('com/delete/<int:pk>/', views.CommentDeleteView.as_view(), name='com_delete'),
]
