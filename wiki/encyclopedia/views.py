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

def search(request):
    if request.method == 'POST':
        query = request.POST['q']
        entries = util.list_entries()
        # if the user's query matches one of the existing wiki entries
        if query in entries:
            return render(request, "encyclopedia/entry.html", {
                'entry_name':query,
                'entry_html_content':markdown2.markdown(util.get_entry(query))
                })
        
        else:
            results=[]  #list of wiki entries for which query is a subsrting

            for entry in entries:
                print(entry, '  ', query) 
                if query in entry:
                    results.append(entry)
            print(results)      
            if results:
                return render(request, "encyclopedia/search.html",{
                    'results':results
                    }) 
            else:
                return  render(request, "encyclopedia/entry.html", {
                'entry_name':'Not Found',
                'not_found':'404 <br> Page Not Found'
                })  


          
    else:
        return render(request, "encyclopedia/entry.html", {
            "search1":"input your query"
        })