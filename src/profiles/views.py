from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, View
from django.http import Http404

from restaurants.models import Restaurant
from menus.models import Item

from .models import Profile
# Create your views here.

User = get_user_model()

class ProfileFollowToggle(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        #print(request.POST)
        user_to_toggle = request.POST.get("username")
        profile_, is_following = Profile.objects.toggle_follow(request.user, user_to_toggle)
        print(is_following)
        return redirect(f"/u/{ profile_.user.username }/")

class ProfileDetailView(DetailView):
    template_name = 'profiles/user.html'

    def get_object(self):
        username = self.kwargs.get("username")
        if username is None:
            raise Http404
        return get_object_or_404(User, username__iexact=username, is_active=True)

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
        user = context['user']
        is_following = False
        if user.profile in self.request.user.is_following.all():
            is_following = True
        context['is_following'] = is_following
        query = self.request.GET.get('q')
        items_exists = Item.objects.filter(user=user).exists()
        qs = Restaurant.objects.filter(owner=user).search(query)
        if items_exists and qs.exists():
            context['locations'] = qs
        return context