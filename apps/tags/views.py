from django.views import generic
from django.urls import reverse_lazy

from apps.tags.models import Tag
from apps.tags.forms import TagForm


class TagListView(generic.ListView):
    model = Tag
    template_name = 'tag/index.html'
    context_object_name = 'tags'


class TagDetailView(generic.DetailView):
    model = Tag
    template_name = 'tag/detail.html'
    context_object_name = 'tag'


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'tag/create.html'
    success_url = reverse_lazy('tag_index')


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'tag/update.html'
    success_url = reverse_lazy('tag_detail')

    def get_success_url(self):
        return reverse_lazy('tag_detail', kwargs={'pk': self.object.pk})


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = 'tag/delete.html'
    success_url = reverse_lazy('tag_index')