from django.shortcuts import render


def home_page(request):
    return render(request, 'home_page.html')


def unauthorized(request):
    return render(request, 'main/unauthorized.html')


def bad_request(request, exception=None):
    return render(request, 'main/bad_request.html')


def permission_denied(request, exception=None):
    return render(request, 'main/permission_denied.html')


def page_not_found(request, exception=None):
    return render(request, 'main/not_found.html')


def server_error(request, exception=None):
    return render(request, 'main/server_error.html')
