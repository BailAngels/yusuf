from django.views import generic
from django.urls import reverse_lazy

from apps.comments.models import Comment
from apps.comments.forms import CommentCreateForm, CommentUpdateForm 


class CommentListView(generic.ListView):
    model = Comment
    template_name = 'comment/comlist.html'
    context_object_name = 'comments'


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentCreateForm
    template_name = 'comment/comcreate.html'
    success_url = reverse_lazy('detail')

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.post.pk})

class CommentDetailView(generic.DetailView):
    model = Comment
    template_name = 'comment/comdetail.html'
    context_object_name = 'comment'


class CommentUpdateView(generic.UpdateView):
    model = Comment
    form_class = CommentUpdateForm
    template_name = 'comment/comupdate.html'
    success_url = reverse_lazy('detail')

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.post.pk})


class CommentDeleteView(generic.DeleteView):
    model = Comment
    template_name = 'comment/comdelete.html'
    success_url = reverse_lazy('detail')

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.post.pk})
