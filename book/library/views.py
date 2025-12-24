from django.shortcuts import redirect, render
from .forms import ContactForm,BookForm
from .models import Book
# Create your views here.

# View to handle regular form (example: Contact form)

def contact_view(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            # Normally you might send an email or save info here
            # For demo just redirect or show success message
            return render(request,'library/contact_success.html',{'data':form.cleaned_data})
    else:
        form=ContactForm()
        return render(request,'library/contact_form.html',{'form':form})

# View to create new Book using ModelForm
def create_book(request):
    if request.method=='POST':
        form=BookForm(request.POST)
        if form.is_valid():
            form.save() # save new Book to database
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request,'library/book_form.html',{'form':form})

#View to list all books

def list_books(request):
    books=Book.objects.all()
    return render(request,'library/book_list.html',{'books':books})
