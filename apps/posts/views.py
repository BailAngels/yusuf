from django.views import generic
from django.urls import reverse_lazy

from apps.posts.models import Post, PostLike
from apps.posts.forms import PostCreateForm, PostUpdateForm


class PostListView(generic.ListView):
    model = Post
    template_name = 'post/index.html'
    context_object_name = 'posts'


class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'post/create.html'
    success_url = reverse_lazy('index')


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post/detail.html'
    context_object_name = 'posts'


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'post/update.html'
    success_url = reverse_lazy('detail')

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.pk})
    

class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'post/delete.html'
    success_url = reverse_lazy('index')


class PostLikeView(generic.CreateView):
    model = PostLike 
    fields = []

    def form_valid(self, form):
        form.instance.belek = Post.objects.get(pk= self.kwargs['pk']) 
        return super().form_valid(form)
    
