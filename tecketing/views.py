from django.http import HttpResponse
from django.shortcuts import render
from tecketing.models import Ticket


def index(request):
    return render(request, 'tecketing/index.html')
    

def index2(request):
    return render(request, 'tecketing/home.html')


def submit(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        body = request.POST.get('body')
        new_ticket = Ticket(submitter=username, body=body)
        new_ticket.save()
        return HttpResponse("Successfully submitted ticket!")
    return render(request, 'tecketing/submit.html')


def tickets(request):
    all_tickets = Ticket.objects.all()
    return render(request, 'tecketing/tickets.html', {'tickets': all_tickets})


def ticket(request, ticket_id):
    selected_ticket = Ticket.objects.get(pk=ticket_id)
    return render(request, 'tecketing/ticket.html', {'ticket': selected_ticket})
