from django.shortcuts import redirect, render, get_object_or_404
from .models import Item, Chat, ChatMessage
from .forms import ChatMessageForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def new_chat(request, id):
    item = get_object_or_404(Item, id=id)

    if item.added_by == request.user:
        return redirect('my_items')

    chats = Chat.objects.filter(item=item).filter(members__in=[request.user.id])
    if chats:
        return redirect('chat:detail_chat', id=chats.first().id)
    if request.method == 'POST':
        form = ChatMessageForm(request.POST or None)

        if form.is_valid():
            chat = Chat.objects.create(item=item)
            chat.members.add(request.user)
            chat.members.add(item.added_by)
            chat.save()

            chat_message = form.save(commit=False)
            chat_message.chat = chat
            chat_message.added_by = request.user
            chat_message.save()

            return redirect('detail', id=id)
    else:
        form = ChatMessageForm()
    return render(request, 'chat/new_chat.html', context={'form':form})

@login_required
def inbox(request):
    chats = Chat.objects.filter().filter(members__in=[request.user.id])
    return render(request, 'chat/inbox.html', context={'chats': chats})

@login_required
def detail_chat(request, id):
    chat = Chat.objects.filter(members__in=[request.user.id]).get(id=id)
    if request.method == 'POST':
        form = ChatMessageForm(request.POST or None)
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.chat = chat
            chat_message.added_by = request.user
            chat_message.save()

            chat.save()
            return redirect('chat:detail_chat', id=id)
        else:
            print(form.errors)
    else:
        form = ChatMessageForm()

    return render(request, 'chat/detail.html', context={'chat':chat,
                                                        'form': form})
