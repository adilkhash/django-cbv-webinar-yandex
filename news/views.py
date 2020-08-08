from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)
from django.http import HttpResponseForbidden
from django.utils.text import slugify
from django.urls import reverse, reverse_lazy
from transliterate import translit
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from news.models import News
from news.forms import NewsModelForm, CommentModelForm


class AdilForbiddenMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.username == 'adil':
            return HttpResponseForbidden('You are not allowed')
        return super().dispatch(request, *args, **kwargs)


class NewsListView(ListView):
    model = News
    template_name = 'index.html'
    paginate_by = 3
    context_object_name = 'news'


class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'news'
    extra_context = {
        'comments_form': CommentModelForm()
    }


class NewsCreateView(LoginRequiredMixin, AdilForbiddenMixin, CreateView):
    model = News
    form_class = NewsModelForm
    template_name = 'news_add.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.author = self.request.user
        news.slug = slugify(translit(news.title, language_code='ru', reversed=True))
        news.save()
        messages.add_message(
            self.request,
            messages.SUCCESS,
            f'Новость {news.title} добавлена',
            extra_tags='success'
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('news:detail_news', kwargs={'slug': self.object.slug})


class NewsUpdateView(LoginRequiredMixin, UpdateView):
    model = News
    form_class = NewsModelForm
    template_name = 'news_form.html'

    @property
    def success_url(self):
        return reverse('news:detail_news', kwargs={'slug': self.object.slug})


class NewsDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'news_delete.html'
    model = News
    success_url = reverse_lazy('news:index')

    def get_context_data(self, **kwargs):
        messages.add_message(
            self.request, messages.INFO, f'Новость {self.object.title} удалена', extra_tags='info'
        )
        return super().get_context_data(**kwargs)


def add_comment(request, slug):
    """Добавление комментария к новости"""
    if request.method == 'POST':
        news = get_object_or_404(News, slug=slug)
        form = CommentModelForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.news = news
            comment.save()
        else:
            return render(request, 'news_detail.html', {
                'news': news,
                'comments': news.comments.all(),
                'comments_form': form
            })
    return redirect(reverse('news:detail_news', kwargs={'slug': slug}))
