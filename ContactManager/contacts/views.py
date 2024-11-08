from django.shortcuts import render,get_object_or_404, redirect
from contacts.models import Contact
from contacts.forms import ContactForm
from django.contrib import messages
# Create your views here.
def contact_list(request):
    contacts=Contact.objects.all()
    return render(request,'contact_list.html',{'contacts':contacts})

def create_contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Contact Created Successfully!')
            return redirect('contact_list')
    else:
        form=ContactForm()
    return render(request,'contact_form.html',{'form':form, 'action':'Create'})

def update_contact(request,pk):
    contact=get_object_or_404(Contact,pk=pk)
    if request.method=='POST':
        form=ContactForm(request.POST,request.FILES,instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request,'Contact updated successfully!')
            return redirect('contact_list')
    else:
        form=ContactForm(instance=contact)
    return render(request,'contact_form.html',{'form':form,'action':'Update'})

def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        messages.success(request, 'Contact deleted successfully!')
        return redirect('contact_list')
    return render(request, 'contact_confirm_delete.html', {'contact': contact})