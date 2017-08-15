from django import forms
from django_select2.forms import (
    HeavySelect2MultipleWidget, HeavySelect2Widget, ModelSelect2MultipleWidget,
    ModelSelect2TagWidget, ModelSelect2Widget, Select2MultipleWidget,
    Select2Widget
    )

from .models import Branch, Equipment

class BranchForm(forms.ModelForm):
    """
    Implementation with vanilla django widgets
    """
    class Meta:
        model = Branch
        fields = ['branchid', 'lineid', 'branchname', 'frombusid', 'tobusid', 'ckt']
        widgets = {
            'lineid': Select2Widget,
            'frombusid': Select2Widget,
            'tobusid': Select2Widget,
        }

class EquipmentForm(forms.ModelForm):
    """
    Implementation with vanilla django widgets
    """
    class Meta:
        model = Equipment
        fields = ['equipmentid', 'branchid', 'busid', 'equipmentname']
        widgets = {
            'branchid': Select2Widget,
            'busid': Select2Widget,
        }


class SelectBranchForm(forms.Form):
    """
    Implementation with Select2 widgets
    """
    branch = forms.ModelChoiceField(
        queryset = Branch.objects.all(),
        widget = ModelSelect2Widget(
                model=Branch,
                search_fields='branchname',
                )
                )
