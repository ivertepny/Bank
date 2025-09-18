# переробив з використанням міксінів для уникнення дублювання коду
from django.contrib.auth.forms import UserChangeForm as DjangoUserChangeForm
from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import User


class RegularUserSecurityMixin:
    """Додає перевірку обов'язковості security_* для не-суперюзерів."""
    def clean(self):
        cleaned_data = super().clean()
        is_superuser = cleaned_data.get("is_superuser")
        security_question = cleaned_data.get("security_question")
        security_answer = cleaned_data.get("security_answer")

        if not is_superuser:
            if not security_question:
                self.add_error(
                    "security_question",
                    _("Security question is required for regular users"),
                )
            if not security_answer:
                self.add_error(
                    "security_answer",
                    _("Security answer is required for regular users"),
                )
        return cleaned_data


class UniqueUserFieldsMixin:
    """Уніфікована перевірка унікальності полів користувача для create/update."""
    _unique_messages = {
        "email": _("A user with that email already exists."),
        "id_no": _("A user with that ID number already exists."),
    }

    def _clean_unique_field(self, field_name: str):
        value = self.cleaned_data.get(field_name)
        if not value:
            return value

        qs = User.objects.filter(**{field_name: value})
        # для форм редагування виключаємо поточного інстанса
        if getattr(self, "instance", None) and getattr(self.instance, "pk", None):
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise ValidationError(self._unique_messages.get(field_name, _("Already exists.")))
        return value

    def clean_email(self):
        return self._clean_unique_field("email")

    def clean_id_no(self):
        return self._clean_unique_field("id_no")


class UserCreationForm(RegularUserSecurityMixin, UniqueUserFieldsMixin, DjangoUserCreationForm):
    class Meta:
        model = User
        fields = [
            "email",
            "id_no",
            "first_name",
            "middle_name",
            "last_name",
            "security_question",
            "security_answer",
            "is_staff",
            "is_superuser",
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user


class UserChangeForm(RegularUserSecurityMixin, UniqueUserFieldsMixin, DjangoUserChangeForm):
    class Meta:
        model = User
        fields = [
            "email",
            "id_no",
            "first_name",
            "middle_name",
            "last_name",
            "security_question",
            "security_answer",
            "is_active",
            "is_staff",
            "is_superuser",
        ]
