from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Client
from .forms import NewClientForm

def client_list(request):
    clients = Client.objects.filter(added_date__lte=timezone.now()).order_by('added_date')
    return render(request, 'manejoclientes/client_list.html', {'clients': clients})

def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'manejoclientes/client_detail.html', {'client': client})

def client_new(request):
	if request.method == "POST":
		form = NewClientForm(request.POST)
		if form.is_valid():
			client = form.save(commit=False)
			#post.author = request.user
			#post.published_date = timezone.now()
			client.save()
			return redirect('manejoclientes.views.client_detail', pk=client.pk)
	else:
		form = NewClientForm()
	return render(request, 'manejoclientes/new_client.html', {'form': form})

def client_edit(request, pk):
        client = get_object_or_404(Client, pk=pk)
        if request.method == "POST":
            form = NewClientForm(request.POST, instance=client)
            if form.is_valid():
                #client = form.save(commit=False)
                client.save()
                return redirect('manejoclientes.views.client_detail', pk=client.pk)
        else:
            form = NewClientForm(instance=client)
        return render(request, 'manejoclientes/new_client.html', {'form': form})