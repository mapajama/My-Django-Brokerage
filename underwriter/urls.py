from django.urls import path
from . import views

urlpatterns = [
    path('list', views.UnderwriterListView.as_view(), name='underwriter_list'),
    path('create', views.UnderwriterCreateView.as_view(), name='underwriter_create'),
    path('<int:pk>/update/', views.UnderwriterUpdateView.as_view(), name='underwriter_update'),
    path('<int:pk>/delete/', views.UnderwriterDeleteView.as_view(), name='underwriter_delete'),
    path('list-client', views.ClientListView.as_view(), name='client_list'),
    path('create_list', views.ClientCreateView.as_view(), name='client_create'),
    path('<int:pk>/update/', views.ClientUpdateView.as_view(), name='client_update'),
    path('<int:pk>/delete/', views.ClientDeleteView.as_view(), name='client_delete'),
]
