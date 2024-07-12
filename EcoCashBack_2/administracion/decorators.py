from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

def role_required(role_name):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')
            if not hasattr(request.user, 'Usuario'):
                raise PermissionDenied
            if request.user.usuario.rol.nombre != role_name:
                raise PermissionDenied
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator