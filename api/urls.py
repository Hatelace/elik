from django.urls import path

from . import views


urlpatterns = [
    path('categories/', views.CategoryListApiView.as_view(), name='categories'),
    path('categories/<str:id>/', views.CategoryDetail.as_view(),
         name='categories_detail'),
    path('products/', views.ProductsListApiView.as_view(), name='products'),
    path('order/', views.OrderView.as_view()),
    path('trdelnik/', views.TrdelnikView.as_view()),
]
