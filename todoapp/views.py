from django.shortcuts import redirect, render
# from userAuth.models import User
from django.contrib.auth.models import User
from .forms import todoItem
from .models import TodoList

# Create your views here.
def home(request, pk):
    try:
        user = User.objects.get(pk=pk)
        try:
            lists = TodoList.objects.filter(user=user)
            form = todoItem()
            return render(request, 'todoapp/home.html', {
                'form': form,
                'lists': lists,
            })
        except TodoList.DoesNotExist:
            form = todoItem()
            return render(request, 'todoapp/home.html', {
                'form': form,
                'lists': [],
            })
    except User.DoesNotExist:
        return redirect('login_page')

def submit(request):
    if request.method == "POST":
        form_contents = todoItem(request.POST)
        userid = request.user.id
        # userid = request.POST.session['user']
        if form_contents.is_valid():
            todoitem = form_contents.save(commit=False)
            user = User.objects.get(pk=userid)
            todoitem.user = user
            todoitem.save()
        return redirect("home_page", userid)
    else:
        return redirect("login_page")