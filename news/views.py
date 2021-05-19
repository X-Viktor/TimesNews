from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as Login
from django.db.models import F
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from news.forms import NewsCreateForm, LoginForm
from news.models import News


class NewsCreateView(LoginRequiredMixin, CreateView):
    """Создание новости."""
    login_url = reverse_lazy('login')
    redirect_field_name = 'next'

    form_class = NewsCreateForm
    template_name = 'news/create-news.html'

    def form_valid(self, form):
        # Добавление автора новости
        form.instance.owner = self.request.user
        return super(NewsCreateView, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse('news_detail', kwargs={'pk': self.object.pk})


class NewsDetailView(DetailView):
    """Отображение подробностей новости."""
    model = News
    context_object_name = 'news'
    template_name = 'news/news-detail.html'

    def get_object(self, queryset=None):
        """Увеличиваем счетчик просмотров."""
        news = super(NewsDetailView, self).get_object(queryset)
        News.objects.filter(pk=news.pk).update(
            views_count=F('views_count') + 1)
        news.views_count += 1
        return news


class NewsListView(ListView):
    """Отображение всех новостей."""
    model = News
    context_object_name = 'news'
    queryset = News.objects.all().prefetch_related('tags')
    template_name = 'news/all-news.html'

    paginate_by = 10


class NewsStatisticsView(ListView):
    """Отображение статистики новостей."""
    model = News
    context_object_name = 'news'
    queryset = News.objects.all().order_by('-views_count')
    template_name = 'news/news-statistics.html'

    paginate_by = 10


class LoginView(Login):
    """Авторизация."""
    form_class = LoginForm
    template_name = 'login.html'
