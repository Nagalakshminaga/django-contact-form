from django.shortcuts import render,redirect
from .models import CommentModel
from .forms import CommentForm
from django.contrib import messages

def home(request):
    
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            
            form.save()
            name = request.POST.get('name')

            try:
                data = CommentModel.objects.get(name=name) #error
                if data:
                    
                    messages.success(request, "Data is stored successfully")
                    return redirect ('home:home')
                else: 
                    pass   
            except:
                messages.error(request, "First Name Already Exists")
                return redirect ('home:home')    
            
        
    else:
        form = CommentForm()        
    context = {
        'form': form
    }
        
    return render(request, 'home.html', context)



