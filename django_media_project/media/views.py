from django.shortcuts import render
from django.http import Http404
from .models import Media


def media_detail(request, index):
    """Display a single media item by zero-based index with its comment."""
    media_list = Media.objects.order_by('id')
    try:
        media = media_list[index]
    except IndexError:
        raise Http404("Media not found")

    total_items = media_list.count()
    context = {
        'media': media,
        'comment': getattr(media, 'comment', None),
        'index': index,
        'prev_index': index - 1 if index > 0 else None,
        'next_index': index + 1 if index + 1 < total_items else None,
    }
    return render(request, 'media/media_detail.html', context)


def media_list(request):
    """Display all media items"""
    media_items = Media.objects.order_by('id')
    context = {
        'media_items': media_items,
    }
    return render(request, 'media/media_list.html', context)
