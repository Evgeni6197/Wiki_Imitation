from django.shortcuts import render

from . import util

import markdown2


def index(request):
    '''
    Renders the home page of the app which contains the whole list of wiki entry pages
    '''
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "title":"Encyclopedia",
        "heading":"All Pages"
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
    '''
    Recieves the search form request and proceeds it.
    Checks if the requested wiki entry page does exist. If so - renders
    the wanted entry. If not - renders the search result page containing
    the list of all existing entries, names of which contain the query as 
    a substring, i.e. for query 'yth' can be 'Python' entry presented.  
    '''

    if request.method == 'POST':

        query = request.POST['q']
        entries = util.list_entries()

        # if the user's query matches one of the existing wiki entries
        if query in entries:

            # renders the wiki page wanted converted from Markdown to HTML
            return render(request, "encyclopedia/entry.html", {
                'entry_name':query,
                'entry_html_content':markdown2.markdown(util.get_entry(query))
                })
        
        # if not - renders search result page
        else:
            results=[]  #list of wiki entry names for which query is a subsrting

            for entry in entries:
                if query in entry:
                    results.append(entry) 

            # if the search result list is not empty - renders the search result page             
            if results:
                return render(request, "encyclopedia/index.html",{
                'entries':results,
                "title":"Search results",
                "heading":"Perhaps you searched"
                 }) 

            # if it is empty - renders "Not found" message     
            else:
                return  render(request, "encyclopedia/entry.html", {
                'title':'Not Found',
                'not_found':'404 <br> Page Not Found'
                })           
    
    # if request method is GET -renders a prompt message
    else:
        return render(request, "encyclopedia/entry.html", {
            "search1":"input your query"
        })


def new_page(request):
    '''
    Creates a new wiki entry page
    '''
    if request.method == 'POST':

        # Getting the name and the content of a new wiki page from 'textarea' HTML tag
        page_name=request.POST['page_name']
        page_content =request.POST['page_content']
        
        # Checking if the name is not empty and not already taken
        if not page_name or page_name in util.list_entries():
            
            # if so, rendering   new page template back with an error message
            return render(request, "encyclopedia/new_page.html",{
            'title':'New Page',
            'text': page_content ,
            'error_message':'Try again: no name entered or this name is taken'
            })
        
        # if the name is unique - saving the new entry as .md file in  the 'entry/' folder
        else:            
            util.save_entry(page_name, page_content)

            # rendering the newly created entry page
            return render(request, "encyclopedia/entry.html", {
                'entry_name':page_name,
                'entry_html_content':markdown2.markdown(util.get_entry(page_name))
            })

    # if request method is GET - rendering the 'Create new page' template of the app
    return render(request, "encyclopedia/new_page.html",{
    'title':'New Page',
    })