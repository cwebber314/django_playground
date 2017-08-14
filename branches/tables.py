"""
Some Questions.  How do we add columns to the table for CRUD stuff
"""
import django_tables2 as tables
from .models import Branch, Line, Equipment
from table.columns import Column
from table import Table

class BranchTable(tables.Table):
    class Meta:
        model = Branch
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}

class LineTable(tables.Table):
    class Meta:
        model = Line
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}

class EquipmentTable(Table):
    """
    Render usint the django-datatable library
    """
    equipmentid = Column(field='equipmentid')
    branchid = Column(field='branchid')
    busid = Column(field='busid')
    equipmentname = Column(field='equipmentname')
    class Meta:
        model = Equipment
        # add class="paleblue" to <table> tag
