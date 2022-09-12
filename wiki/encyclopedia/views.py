from django.shortcuts import render

from . import util

import markdown2


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry_name):
    '''
    Renders Wiki Entry page converted from Markdown to HTML. 
    If the Page does not exist renders 'Not Found' page instead. 
    '''
    try:
        return render(request, "encyclopedia/entry.html", {
            'entry_name':entry_name,
            'entry_html_content':markdown2.markdown(util.get_entry(entry_name))
        })
    except TypeError:
        return render(request, "encyclopedia/entry.html", {
            'entry_name':'Not Found',
            'not_found':'404 <br> Page Not Found'
        })        