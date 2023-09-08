from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views import View
from hitcount.views import HitCountDetailView

from .models import Post
from .forms import CommentForm


class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = "-date_posted"
    paginate_by = 5


class CommentGet(HitCountDetailView):
    model = Post
    template_name = "blog/post_detail.html"
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(CommentGet, self).get_context_data(**kwargs)
        context["form"] = CommentForm()
        context["form.instance.author"] = self.request.user
        return context


class CommentPost(LoginRequiredMixin, SingleObjectMixin, FormView):
    model = Post
    form_class = CommentForm
    template_name = "blog/post_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        comment = form.save(commit=False)
        comment.post = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        post = self.get_object()
        return reverse("blog:post_detail", kwargs={"pk": post.pk})


class PostDetailView(View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)


def about_view(request):
    return render(request, "blog/about.html", {})
