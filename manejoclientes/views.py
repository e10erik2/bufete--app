from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Client

def client_list(request):
    clients = Client.objects.filter(added_date__lte=timezone.now()).order_by('added_date')
    return render(request, 'manejoclientes/client_list.html', {'clients': clients})

def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'manejoclientes/client_detail.html', {'client': client})