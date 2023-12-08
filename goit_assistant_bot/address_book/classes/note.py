import re
from colorama import Fore, Style
from ..constants import TEXT
from ..exceptions import ValidationValueExseption
from .field import Field

class NoteContent(Field):
    def __init__(self, value = ""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if len(new_value) > 10 and len(new_value) <= 100:
            self._value = new_value
        else:
            raise ValidationValueExseption(TEXT["NOTE_VALIDATION"])

    def __str__(self):
        return f'{self._value}'

    def __repr__(self):
        return f'Note: {self._value}'


class Tag(Field):
    def __init__(self, value = ""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if re.search(r"\w{1,15}", new_value):
            self._value = new_value
        else:
            raise ValidationValueExseption(TEXT["TAG_VALIDATION"])

    def __str__(self):
        return f'{self._value}'

    def __repr__(self):
        return f'Tag: {self._value}'

class Note:
    def __init__(self, content):
        self.content = NoteContent(content)
        self.tags = []

    def get_tags(self, no_data_message = "NO TAGS"):
        return " ".join("#" + str(tag) for tag in self.tags) if len(self.tags) > 0 else no_data_message

    def find_tag(self, tag):
        tags = list(filter(lambda t: t.value.lower() == tag.lower(), self.tags))
        return len(tags) > 0

    def remove_tag(self, tag):
        if self.find_tag(tag):
            self.tags = list(filter(lambda t: t.value.lower() != tag.lower(), self.tags))
            print(Fore.GREEN + TEXT["TAG_REMOVED"] + Style.RESET_ALL)
            return True
        
        print(Fore.LIGHTBLACK_EX + TEXT["TAG_NOT_FOUND"] + Style.RESET_ALL)
        return False

    def add_tag(self, tag):
        if self.find_tag(tag):
            print(Fore.LIGHTBLACK_EX + TEXT["TAG_EXISTS"] + Style.RESET_ALL)
            return False

        self.tags.append(Tag(tag))
        print(Fore.GREEN + TEXT["TAG_ADDED"] + Style.RESET_ALL)
        return True

    def get_content(self, no_data_message = ""):
        return self.content.value if self.content else no_data_message

    def __str__(self):
        return self.get_tags() + "\n" + self.get_content()

__all__ = ["Note"]