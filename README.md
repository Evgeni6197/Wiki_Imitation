# Wiki_Imitation
## [Demonstration video](https://youtu.be/ZUncrEivXnU)
***

## Description  


It is imitated Wiki home page. The options like *search* field, *create new page , edit page* and *random page* are implemented. It is realized functionality  to present search results  as a list of entries, where the query is a substring of the name of every resuting page. The page content while creating or editing is beeing  entered using [Markdown](https://www.markdownguide.org/basic-syntax) syntax. All "Wiki" entries used in the project are saved in the *entries/* folder as *.md* files.


***

## Launching

To launch the project  it is needed to install [Django]( https://www.djangoproject.com) first.


Then type in your local terminal in your choosed folder   
```
git clone https://github.com/Evgeni6197/Wiki_Imitation.git
```
enter the project folder  
```
 cd Wiki_Imitation/wiki
```
run django server locally  

```
 python manage.py runserver
```

Ignore warning about unapplied migrations.  In your local browser in url

```
localhost:8000/wiki
```
you can find the project home page.

