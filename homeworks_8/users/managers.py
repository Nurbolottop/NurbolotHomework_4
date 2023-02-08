from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Кастомная модель менеджера, которая создает пользователей и суперюзера.
    Аутентификация происходит по email вместо username
    """

    def create_user(self, email, password, **extra_fields):
        """
        Метод создания обычного пользователя
        """
        if not email:
            raise ValueError("Email должен быть задан обязательно!")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Создание и сохранение суперпользователя
        """

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Суперюзер должен иметь is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Суперюзер должен иметь is_superuser=True")
        superuser = self.create_user(email, password, **extra_fields)
        return superuser
