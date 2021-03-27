from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from .models import Post, Files
from .forms import FeedModelForm, FileModelForm


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('posts:home'))


class TweetListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-create_date']


def create_post(request):
    if request.method == 'POST':
        author = request.user
        print('posting')
        post_form = FeedModelForm(request.POST)
        file_form = FileModelForm(request.POST, request.FILES)
        files = request.FILES.getlist('file')
        if post_form.is_valid() and file_form.is_valid():
            post_instance = post_form.save(commit=False)

            post_instance.author = author

            post_instance.save()
            file_instance = file_form.save(commit=False)
            #            file_instance.post = post_instance
            #          file_instance.save()

            for f in files:
                file_instance.post = Files(file=f, post=post_instance).save()

        return redirect('/home/')
    else:
        post_form = FeedModelForm()
        file_form = FileModelForm()
        return render(request, 'create.html', {'post_form': post_form, 'file_form': file_form})


'''class TweetCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'create.html'
    fields = ['media', 'body', 'topic']
    success_url = '/home'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)'''


class TweetUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'create.html'
    fields = ['body', 'topic']
    success_url = '/home'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class TweetDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'tweet_confirm_delete.html'
    fields = ['body']
    success_url = '/home'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
