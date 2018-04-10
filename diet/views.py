from django.shortcuts import render
from django.views.generic.base import View


class StartPageView(View):
    def get(self, request):
        return render(request, template_name='base.html')