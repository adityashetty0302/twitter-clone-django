from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from . import forms
from .models import Tweets
from accounts.models import Following
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


class CreateTweet(LoginRequiredMixin, generic.CreateView):
    fields = ('tweet',)
    model = Tweets

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class MyTweets(generic.ListView):
    model = Tweets

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get("username"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tweet_user"] = self.kwargs.get("username")
        return context


# class TweetDelete(LoginRequiredMixin, generic.DeleteView):
#     model = Tweets
#     success_url = reverse_lazy("delete:delete-success")
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset.filter(user_id=self.request.user.id)


def delete_tweet(request, pk):
    tweet_obj = get_object_or_404(Tweets, pk=pk, user__username=request.user.username)
    tweet_obj.delete()
    return render(request, 'tweets/tweets_delete_success.html')


class DeleteSuccess(LoginRequiredMixin, generic.TemplateView):
    template_name = 'tweets/tweets_delete_success.html'

class HomeTweets(generic.ListView):
    model = Tweets
    template_name = 'tweets/tweets_list_home.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__id__in=Following.objects.filter(current_user=self.kwargs.get("pk")).values('target'))
