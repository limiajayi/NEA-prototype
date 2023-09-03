from students.models import StudentUser
from django.shortcuts import redirect

def user_login_required(function):
    def wrapper(request, login_url='http://127.0.0.1:8000/home/login/', *args, **kwargs):
        if not 'user_id' in request.session:
            return redirect(login_url)
        else:
            return function(request, *args, **kwargs)
    return wrapper