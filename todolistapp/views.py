from django.shortcuts import render
from django.utils import timezone
from .models import Todo
from django.http import HttpResponseRedirect

# Create your views here.
def items(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    send_to_front = {
        'todo_items' : todo_items,
    }

    return render(request, 'todo/index.html', send_to_front)

def add(request):
    current_added_date = timezone.now()
    content = request.POST['content']
    Todo.objects.create(added_date = current_added_date, text = content)
    return HttpResponseRedirect('/')

def delete_item(request, item_id):
    Todo.objects.get(id=item_id).delete()
    return HttpResponseRedirect('/')
