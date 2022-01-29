from django.urls import path
from . import views
urlpatterns = [
    path("", views.BlogsTemplateView.as_view(), name="blogs"),

    path("<category_id>/", views.CategoryblogsView.as_view(), name="category_blogs"),
    path("<pk>/<slug>/", views.BlogsDetail.as_view(), name="single_blogs"),
    
]