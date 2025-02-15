from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from blog.models import Blog
class BlogListView(ListView):
    model = Blog
    template_name = 'blog_list.html'

    def get_queryset(self):
        return Blog.objects.filter(is_publication=True)


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.counter += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ['name', 'description', 'image', 'is_publication']
    template_name = 'blog_form.html'
    success_url = reverse_lazy('blog:blog_list')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['name', 'description', 'image', 'is_publication']
    template_name = 'blog_form.html'
    success_url = reverse_lazy('blog:blog_detail')

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog_confirm_delete.html'
    success_url = reverse_lazy('blog:blog_list')
