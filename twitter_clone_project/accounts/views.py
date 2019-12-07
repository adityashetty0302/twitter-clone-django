from django.urls import reverse_lazy
from django.views import generic
from .forms import UserCreateForm
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from .models import Following

User = get_user_model()


class SignUp(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


class IndexPage(generic.TemplateView):
    template_name = 'index.html'


class ThanksPage(generic.TemplateView):
    template_name = 'thanks.html'


class AllUsers(generic.ListView):
    model = User

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.exclude(username__iexact=self.request.user.username)


def change_follow_status(request):
    status = request.GET.get('status', None)
    username = request.GET.get('username', None).strip('@')

    if status == 'Follow':
        target_user_obj = User.objects.get(username=username)
        Following.objects.create(current_user=request.user, target=target_user_obj)
        data = {'status': 'Unfollow'}
    else:
        target_user_obj = User.objects.get(username=username)
        Following.objects.get(current_user=request.user, target=target_user_obj).delete()
        data = {'status': 'Follow'}

    return JsonResponse(data)


def check_follow_status(request):
    status = request.GET.get('status', None)
    username = request.GET.get('username', None).strip('@')
    target_user_obj = User.objects.get(username=username)
    try:
        Following.objects.get(current_user=request.user, target=target_user_obj)
        data = {'status': 'Unfollow'}
    except Following.DoesNotExist:
        data = {'status': 'Follow'}

    return JsonResponse(data)
