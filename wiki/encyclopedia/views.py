from django.shortcuts import render
from . import util
from .util import get_entry, list_entries
import markdown2
from markdown2 import markdown_path


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, name):
    if request.method == "GET":
        name = name.lower()
        entries = util.list_entries()
        entries_l = [entry.lower() for entry in entries]

        if name in entries_l:
            return render(request, "encyclopedia/wiki.html", {
            "name": name.capitalize(),
            "content": markdown2.markdown(util.get_entry(name))
            })
        else:
            return render(request, "encyclopedia/error.html", {
                "name": name.capitalize(),
            })