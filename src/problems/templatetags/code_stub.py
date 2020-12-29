from pathlib import Path

from django import template
from django.contrib.staticfiles.storage import staticfiles_storage

register = template.Library()

file_extension = {
    "python": "py",
    "julia": "jl",
    "javascript": "js",
    "c": "c"
}

@register.simple_tag
def stringify_code_stub(problem_name, language):
    code_stub_filepath = staticfiles_storage.path(f"code_stubs/{language}/{problem_name}.{file_extension[language]}")
    return Path(code_stub_filepath).read_text()
