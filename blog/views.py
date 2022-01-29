from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views.generic import (
    TemplateView,
    DeleteView,
    UpdateView,
    CreateView,
    ListView,
    DetailView,
)
from blog.models import Category,Blogs,Comment
from portfolio.models import Aboutme

# Create your views here.
class CategoryblogsView(View):
    def get(self, request, category_id, *args, **kwargs):
        template_name = "blog/category.html"
        category = get_object_or_404(Category, pk=category_id)
        category_blogs_list = Blogs.objects.filter(category=category)
        return render(
            request, template_name, {"category_blogs_list": category_blogs_list, "category": category}
        )


class BlogsTemplateView(TemplateView):
    template_name = "blog/blog.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        category_blogs_list = {}
        for category in categories:
            category_blogs_list[category] = Blogs.objects.filter(category=category)
        context["blogs_list"] = Blogs.objects.all().order_by("-created_at")[:4]
        context["trending_blogs"] = Blogs.objects.order_by("-count")
        context["datas"] = Aboutme.objects.all()
        context["category_blogs_list"] = category_blogs_list
        return context


class BlogsDetail(DetailView):
    model = Blogs
    template_name = "blog/single_blogs.html"
    context_object_name = "detail_blogs"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.count = self.object.count + 1
        self.object.save()
        context["popular_blogs"] = Blogs.objects.order_by("-count")[:4]
        return context

@login_required
@require_http_methods(["POST"])
def blogs_feedback(request, *args, **kwargs):
    data = request.POST
    blogs_id = kwargs.get("pk")
    news = get_object_or_404(Blogs, id=blogs_id)
    comment = Comment(blogs=Blogs, feedback=data["feedback"], commenter=request.user)
    comment.save()
    template_name = "blog/comments.html"
    return render(request, template_name, {"comment": comment})
