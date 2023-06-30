from django.urls import path

from . import views

urlpatterns = [
    path('', views.TmListView.as_view(), name='home'),
    path('table/', views.TableListView.as_view(), name='table'),
    path('profile/', views.EmpCreateView.as_view(), name='profile'),
    path('table/employe/<int:pk>/update', views.EmpUpdView.as_view(), name='update'),
    path('table/employe/<int:pk>/delete', views.EmpDelView.as_view(), name='delete'),
]