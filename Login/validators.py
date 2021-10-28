import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

class ContainsDigit:
    def __init__(self, min_digits=0):
        self.min_digits = min_digits

    def validate(self, password, user=None):
        if re.search('[0-9]',password):
            print("bien")
        else:
            raise ValidationError(
                _("Su contraseña debe de contener al menos un digito."),
                code='password_no_number',
                params={'min_digits': self.min_digits},
            )

    def get_help_text(self):
        return _(
            "Su contraseña debe de contener al menos un digito."
            % {'min_digits': self.min_digits}
        )

class ContainsMayus:
    def __init__(self, min_length=0):
        self.min_length = min_length

    def validate(self, password, user=None):
        if re.search('[A-Z]',password):
            print("bien")
        else:
            raise ValidationError(
                _("Su contraseña debe de contener al menos una mayúscula."),
                code='password_no_upper',
                params={'min_length': self.min_length},
            )

    def get_help_text(self):
        return _(
            "Su contraseña debe de contener al menos una mayúscula."
            % {'min_length': self.min_length}
        )
