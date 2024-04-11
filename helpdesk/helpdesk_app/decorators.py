from django.shortcuts import redirect
from django.http import HttpResponse

# pass roles
def allowed_users(allowed_roles=[]):
    # pass in view function
    # decorator placed at top of views
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('access-denied')  # Redirect to an access denied page or login page
        return wrapper_func
    return decorator
