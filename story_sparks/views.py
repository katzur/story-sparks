from django.shortcuts import render


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def handler500(request, *args, **argv):
    """[Handler for internal server error generic message 500]"""
    return render(request, "500.html", status=500)