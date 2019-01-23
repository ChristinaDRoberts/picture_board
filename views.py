from django.shortcuts import render

from django.views.generic import TemplateView

#import class created in Models

from .models import Image

#class for url.py view

class Image_Board(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        images = Image.objects.all()

        context = {
            "images" : images
        }

        return context