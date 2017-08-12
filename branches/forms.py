from django import forms
from django_select2.forms import (
    HeavySelect2MultipleWidget, HeavySelect2Widget, ModelSelect2MultipleWidget,
    ModelSelect2TagWidget, ModelSelect2Widget, Select2MultipleWidget,
    Select2Widget
    )

from .models import Branch

class _BranchesForm(forms.Form):
    """
    Implementation with vanilla django widgets
    """
    branchid = forms.IntegerField(label='Branch ID', required=False)
    branchid2 = forms.ChoiceField(label='Branch ID Choice', required=False)

class BranchesForm(forms.Form):
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
