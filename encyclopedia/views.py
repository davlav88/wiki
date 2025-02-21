from django.shortcuts import render
from . import util
from .util import get_entry, list_entries, save_entry
import markdown2
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })

def wiki(request, name):
    entries = util.list_entries()
    entries_l = [entry.lower() for entry in entries]

    if request.method == "GET":
        name = name.lower()

        if name in entries_l:
            return render(request, "encyclopedia/wiki.html", {
            "name": name.capitalize(),
            "content": markdown2.markdown(util.get_entry(name))
            })
        else:
            message = "not found"
            return render(request, "encyclopedia/error.html", {
                "name": name.capitalize(),
                "message": message
            })


def search(request):
    if request.method == "POST":
        name = request.POST.get("q").lower()
        entries = util.list_entries()
        entries_l = [entry.lower() for entry in entries]
        entries_sub = []

        if name in entries_l:
            return render(request, "encyclopedia/wiki.html", {
                "name": name.capitalize(),
                "content": markdown2.markdown(util.get_entry(name))
            })
        else:
            for entry in entries_l:
                if name in entry:
                    entries_sub.append(entry)
            return render(request, "encyclopedia/results.html", {
                "entries_sub": entries_sub
            })


def create(request):
    if request.method == "GET":
        return render(request, "encyclopedia/create.html")

    if request.method == "POST":
        name = request.POST.get("entry")
        name_h1 = "#" + name.capitalize()
        content = name_h1 + "\n" + request.POST.get("entry_content")
        entries = util.list_entries()
        entries_l = [entry.lower() for entry in entries]

        if name.lower() in entries_l:
            message = "already exists"
            return render(request, "encyclopedia/error.html", {
                "name": name,
                "message": message
            })
        else:
            save_entry(name, content)

        return render(request, "encyclopedia/wiki.html", {
            "name": name,
            "content": markdown2.markdown(util.get_entry(name))
        })

def edit(request):
    if request.method == "GET":
        name = request.GET.get("name")
        content = util.get_entry(name)

        return render(request, "encyclopedia/edit.html", {
            "name": name,
            "content": content
        })
    if request.method == "POST":
        name = request.POST.get("entry")
        content = request.POST.get("entry_content")

        save_entry(name, content)

        return render(request, "encyclopedia/wiki.html", {
            "name": name,
            "content": markdown2.markdown(util.get_entry(name))
        })

def random_pick(request):
    if request.method == "GET":
        entries = util.list_entries()
        name = random.choice(entries)
        content = get_entry(name)

        return render(request, "encyclopedia/wiki.html", {
            "name": name,
            "content": markdown2.markdown(util.get_entry(name))
        })
