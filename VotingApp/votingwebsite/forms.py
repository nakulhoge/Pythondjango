from django import forms
from bootstrap_modal_forms.forms import BSModalForm
from .models import Vote

class VoteSuccessForm(BSModalForm):
    success_message = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Vote
        fields = ['success_message']