from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Book 
from .forms import BookForm
from django.db import connection

# Create your views here.
def index_view(request):
#    books = Book.objects.all()
#    context = {'books':books}
#    return render(request, 'index.html', context)
    book = ""
    
    for row in Book.objects.all():
        book += '''
             <form method='post' action="/update">
             <tr>
                <th>'''+str(row.id)+'''</th>
                <th><input type="text" value="'''+str(row.isbn)+'''"></th>
                <th><input type="text" value="'''+str(row.book_name)+'''"></th>
                <th><input type="text" value="'''+str(row.price)+'''"></th>
                <th><input type="text" value="'''+str(row.author)+'''"></th>
                <th><a href="update/?id='''+str(row.id)+'''"><input type=submit value=update></a></th>
                <th><a href="delete/?id='''+str(row.id)+'''"><input type=button value=delete></a></th>
             </tr>
             </form>
             '''
    
    message = """<html>
                        <head></head>
                        <body>
                            <h1>BOOK</h1>
                            <a href="newbook">Add new book</a>
                            <table border="1">
                                """+book+"""
                            </table>
                        </body>
                    </html>"""
    return HttpResponse(message)
    

def newbook_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            i = form.cleaned_data['isbn']
            n = form.cleaned_data['book_name']
            p = form.cleaned_data['price']
            a = form.cleaned_data['author']
            book = Book(isbn=i, 
                        book_name=n,
                        price=p,
                        author=a)
            book.save()
            return HttpResponseRedirect('/')
    else:
        form = BookForm()
        return render(request, 'newbook.html',{'form':form})
        
    
            

def update(request):
    book_id = request.GET.get('id','')
    
    with connection.cursor() as cursor:
        cursor.execute("UPDATE Books SET book_name='XX', password='P3XX', email='E3XX' where id=%s", book_id)
        cursor.execute("SELECT * FROM Books WHERE id = %s", book_id)
        row = cursor.fetchone()
        
    return HttpResponse(row)

def delete(request):
    book_id = request.GET.get('id','')
    query = Book.objects.get(pk=book_id)
    query.delete()
    return HttpResponseRedirect('/')