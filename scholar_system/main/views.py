from django.shortcuts import render


def home_page(request):
    return render(request, 'home_page.html')


def unauthorized(request):
    return render(request, 'main/unauthorized.html')


def handler404(request, *args, **kwargs):
    response = render(request, 'main/not_found.html')
    response.status_code = 404
    return response


def handler500(request, *args, **kwargs):
    response = render(request, 'main/server_error.html')
    response.status_code = 500
    return response
