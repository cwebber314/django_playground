# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django_tables2 import RequestConfig
from django_tables2 import SingleTableView
from django_filters.views import FilterView
from django_select2.forms import Select2Widget
import django_filters
from django.views.generic.edit import UpdateView, FormView, CreateView
from django.views.generic import ListView
from django.urls import reverse, reverse_lazy


from .models import Line, Branch, Equipment
from .tables import BranchTable, LineTable, EquipmentTable
from .forms import SelectBranchForm, BranchForm, EquipmentForm

def branches2(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SelectBranchForm(request.POST)
        # check whether it's valid:
        # TODO: Allow selection.
        if form.is_valid():
            branch = form.cleaned_data['branch'].branchid
            if branch is None:
                table = BranchTable(Branch.objects.all())
            else:
                table = BranchTable(Branch.objects.filter(branchid=branch))

    # if a GET (or any other method) we'll create a blank form
    elif request.method == 'GET':
        form = SelectBranchForm()
        table = BranchTable(Branch.objects.all())

    return render(request, 'branches/branches2.html', {'form': form, 'table': table})

def index(request):
    return HttpResponse("Hello, world. You're at the branches index.")

class BranchFilter(django_filters.FilterSet):
    branchname = django_filters.ModelChoiceFilter(
                queryset=Branch.objects.all(),
                widget=Select2Widget)
    class Meta:
        model = Branch
        fields = ['branchname']
        #exclude = []

class BranchView(UpdateView):
    """
    With select2 widgets
    """
    form = BranchForm
    form_class = BranchForm
    model = Branch
    template_name = 'branches/branch_update_form.html'

class BranchUpdate(UpdateView):
    """
    With vanilla widgets
    """
    form = BranchForm
    model = Branch
    fields = ['branchid', 'lineid', 'branchname', 'frombusid', 'tobusid', 'ckt']
    template_name = 'branches/branch_update_form.html'

class EquipmentUpdate(UpdateView):
    """
    With select2 widgets.

    Is it possible to save things like table sort order?  It is all javascript
    so I don't know how it would be saved.
    """
    form = EquipmentForm
    form_class = EquipmentForm # Super important variable
    model = Equipment
    template_name = 'branches/equipment_update_form.html'
    success_url = reverse_lazy('equipment5')

class BranchList(ListView):
    template_name = 'branches/branch_list.html'
    model = Branch

class BranchCreate(CreateView):
    model = Branch
    template_name = 'branches/branch_create.html'
    fields = ['branchid', 'lineid', 'branchname', 'frombusid', 'tobusid', 'ckt']
    # TODO: Redirect to branchlist on sucess
    # success_url

class BranchesView(SingleTableView, FilterView):
    model = Branch
    queryset = Branch.objects.all()
    table_class = BranchTable
    template_name = 'branches/branches.html'

    def get_queryset(self, **kwargs):
        return Branch.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BranchesView, self).get_context_data(**kwargs)
        filter = BranchFilter(self.request.GET, queryset=self.get_queryset(**kwargs))
        #filter.form.helper = FooFilterFormHelper()
        table = BranchTable(filter.qs)
        RequestConfig(self.request).configure(table)
        context['filter'] = filter
        context['table'] = table
        return context

def lines(request):
    table = LineTable(Line.objects.all())
    RequestConfig(request).configure(table)
    template_name = 'branches/lines.html'
    return render(request, template_name, {'table': table})


def equipment(request):
    """
    Render equipment manually in a simple table
    """
    template_name = 'branches/equipment.html'
    equipment = Equipment.objects.all()
    #queryset = Branch.objects.all()
    return render(request, template_name, {'equipment': equipment})


def equipment2(request):
    """
    Render equipment manually in a data table with sort.
    """
    template_name = 'branches/equipment2.html'
    equipment = Equipment.objects.all()
    #queryset = Branch.objects.all()
    return render(request, template_name, {'equipment': equipment})


def equipment3(request):
    """
    Equipment table with editable field, but no database connection
    """
    template_name = 'branches/equipment3.html'
    equipment = Equipment.objects.all()
    #queryset = Branch.objects.all()
    return render(request, template_name, {'equipment': equipment})

def equipment4(request):
    """
    Equipment table with editable field.  With database connection
    """
    template_name = 'branches/equipment4.html'
    equipment = Equipment.objects.all()
    #queryset = Branch.objects.all()
    return render(request, template_name, {'equipment': equipment})

def equipment5(request):
    """
    Data table using edit buttons
    """
    template_name = 'branches/equipment5.html'
    equipment = Equipment.objects.all()
    #queryset = Branch.objects.all()
    return render(request, template_name, {'equipment': equipment})
