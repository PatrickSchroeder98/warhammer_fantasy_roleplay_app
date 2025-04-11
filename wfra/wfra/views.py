from django.views.generic import TemplateView
from django.http import JsonResponse
from utils.utils import CAREER_OPTIONS, CAREER_PATHS


class HomePage(TemplateView):
    template_name = "index.html"


class AboutPage(TemplateView):
    template_name = "about.html"


def career_options_api(request):
    return JsonResponse(CAREER_OPTIONS)


def career_paths_api(request):
    return JsonResponse(CAREER_PATHS)
