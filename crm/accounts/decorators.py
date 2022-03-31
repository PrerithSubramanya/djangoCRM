from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated(view_function):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_function(request, *args, **kwargs)

    return wrapper


def userPermission(viewFunc):
    def wrapperFunc(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group == 'admin':
                return viewFunc(request, *args, **kwargs)
            elif group == 'customer':
                return redirect('user')
    return wrapperFunc


