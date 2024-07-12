from functools import wraps
from flask import  session, flash, redirect, url_for


def check_user_role(required_role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user_rol = session.get('rol')
            if user_rol != required_role:
                flash('Acceso no autorizado', 'error')
                return redirect(url_for('login_BP.login'))
            return func(*args, **kwargs)
        return wrapper
    return decorator


