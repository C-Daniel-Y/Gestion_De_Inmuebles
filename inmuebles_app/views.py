from django.shortcuts import render


def home(request):
    """Render the public welcome page."""
    return render(request, 'index.html')


def not_found(request, exception=None):
    """Render the branded 404 page for missing routes."""
    return render(request, '404.html', status=404)
