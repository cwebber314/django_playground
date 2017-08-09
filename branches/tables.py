# tutorial/tables.py
import django_tables2 as tables
from .models import Branch, Line, Equipment

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

class EquipmentTable(tables.Table):
    class Meta:
        model = Equipment
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}
