# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django_tables2 import RequestConfig
from django_tables2 import SingleTableView
from django_filters.views import FilterView
from django_select2.forms import Select2Widget
import django_filters


from .models import Line, Branch, Equipment
from .tables import BranchTable, LineTable, EquipmentTable
from .forms import BranchesForm

def branches2(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BranchesForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            branch = form.cleaned_data['branch']
            if branch is None:
                table = BranchTable(Branch.objects.all())
            else:
                table = BranchTable(Branch.objects.filter(branch=branch))

    # if a GET (or any other method) we'll create a blank form
    elif request.method == 'GET':
        form = BranchesForm()
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

class BranchView(SingleTableView, FilterView):
    model = Branch
    queryset = Branch.objects.all()
    table_class = BranchTable
    template_name = 'branches/branches.html'

    def get_queryset(self, **kwargs):
        return Branch.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BranchView, self).get_context_data(**kwargs)
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
    template_name = 'branches/equipment.html'
    table = EquipmentTable(Equipment.objects.all())
    RequestConfig(request).configure(table)
    return render(request, template_name, {'table': table})
