from django.contrib.auth import get_user_model
from db.models import User

User = get_user_model()


def create_user(
    username: str,
    password: str | None = None,
    email: str | None = None,
    first_name: str | None = None,
    last_name: str | None = None,
    **extra_fields,
) -> User:
    kwargs = {}
    if email is not None:
        kwargs["email"] = email
    if first_name is not None:
        kwargs["first_name"] = first_name
    if last_name is not None:
        kwargs["last_name"] = last_name

    kwargs.update(extra_fields)

    return User.objects.create_user(
        username=username, password=password, **kwargs
    )


def get_user(user_id: int) -> User:
    return User.objects.get(id=user_id)


def update_user(user_id: int, **kwargs) -> User:
    user = get_user(user_id)
    password = kwargs.pop("password", None)

    if password:
        user.set_password(password)

    for key, value in kwargs.items():
        setattr(user, key, value)

    user.save()
    return user
