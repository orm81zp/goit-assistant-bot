import re
from .field import Field
from ..exceptions import ValidationValueExseption
from ..constants import TEXT


class Phone(Field):
    def __init__(self, value = ""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if re.search(r"^\+?[0-9]{12}$", new_value):
            self._value = new_value
        else:
            raise ValidationValueExseption(TEXT["PHONE_VALIDATION"])

    def __str__(self):
        return f'{self._value}'

    def __repr__(self):
        return f'Phone: {self._value}'


__all__ = ["Phone"]
