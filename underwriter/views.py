from django.shortcuts import render, redirect
from .models import Underwriter, Client, ClassDef
from .forms import UnderwriterForm, ClientForm, ClassDefForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


def new_file(request):
    my_dict = {"insert_me": "I am from views.py"}
    return render(request, 'new_file.html', context=my_dict)


def underwriter_list(request):
    underwriters = Underwriter.objects.all()
    return render(request, 'underwriter_list.html', {'underwriters': underwriters})


def underwriter_create(request):
    if request.method == 'POST':
        form = UnderwriterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('underwriter_list')
    else:
        form = UnderwriterForm()
    return render(request, 'underwriter_form.html', {'form': form})


def underwriter_update(request, pk):
    underwriter = Underwriter.objects.get(pk=pk)
    if request.method == 'POST':
        form = UnderwriterForm(request.POST, instance=underwriter)
        if form.is_valid():
            form.save()
            return redirect('underwriter_list')
    else:
        form = UnderwriterForm(instance=underwriter)
    return render(request, 'underwriter_form.html', {'form': form})


def underwriter_delete(request, pk):  # add 'request' parameter
    underwriter = Underwriter.objects.get(pk=pk)
    underwriter.delete()
    return redirect('underwriter_list')


class UnderwriterListView(ListView):
    model = Underwriter
    context_object_name = 'underwriters'
    template_name = 'underwriter_list.html'


class UnderwriterCreateView(CreateView):
    model = Underwriter
    form_class = UnderwriterForm
    success_url = reverse_lazy('underwriter_list')
    template_name = 'underwriter_form.html'


class UnderwriterUpdateView(UpdateView):
    model = Underwriter
    form_class = UnderwriterForm
    success_url = reverse_lazy('underwriter_list')
    template_name = 'underwriter_form.html'


class UnderwriterDeleteView(DeleteView):
    model = Underwriter
    success_url = reverse_lazy('underwriter_list')
    template_name = 'underwriter_confirm_delete.html'


def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})


def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'client_form.html', {'form': form})


def client_update(request, pk):
    client = Client.objects.get(pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'client_form.html', {'form': form})


def client_delete(request, pk):  # add 'request' parameter
    client = Client.objects.get(pk=pk)
    client.delete()
    return redirect('client_list')


class ClientListView(ListView):
    model = Client
    context_object_name = 'clients'
    template_name = 'client_list.html'


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client_list')
    template_name = 'client_form.html'


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client_list')
    template_name = 'client_form.html'


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('client_list')
    template_name = 'client_confirm_delete.html'


def class_def_view(request):
    # Retrieve all ClassDef objects from the database
    class_defs = ClassDef.objects.all()

    # Render the template with the retrieved ClassDef objects
    return render(request, 'class_def.html', {'class_defs': class_defs})


def classdef_create(request):
    form = ClassDefForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('classdef_list')
    return render(request, 'classdef_create.html', {'form': form})


def classdef_update(request, pk):
    classdef = ClassDef.objects.get(pk=pk)
    form = ClassDefForm(request.POST or None, instance=classdef)
    if form.is_valid():
        form.save()
        return redirect('classdef_list')
    return render(request, 'classdef_update.html', {'form': form})


def classdef_delete(request, pk):
    classdef = ClassDef.objects.get(pk=pk)
    if request.method == 'POST':
        classdef.delete()
        return redirect('classdef_list')
    return render(request, 'classdef_delete.html', {'classdef': classdef})


def classdef_list(request):
    classdefs = ClassDef.objects.all()
    return render(request, "classdef_list.html", {'classdefs': classdefs})


class ClassDefListView(ListView):
    model = ClassDef
    template_name = 'classdef_list.html'
    context_object_name = 'classdefs'


class ClassDefCreateView(CreateView):
    model = ClassDef
    form_class = ClassDefForm
    template_name = 'classdef_create.html'
    success_url = reverse_lazy('classdef_list')


class ClassDefUpdateView(UpdateView):
    model = ClassDef
    form_class = ClassDefForm
    template_name = 'classdef_update.html'
    success_url = reverse_lazy('classdef_list')


class ClassDefDeleteView(DeleteView):
    model = ClassDef
    template_name = 'classdef_delete.html'
    success_url = reverse_lazy('classdef_list')
