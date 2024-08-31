from django import forms
from .models import Request

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['title', 'resolve_time_seconds', 'status']
        widgets = {
            'status': forms.Select(choices=Request.STATUS_CHOICES)
        }

    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get("status")
        resolve_time_seconds = cleaned_data.get("resolve_time_seconds")

        if status == 'resolved':
            self.add_error('status', "Заявка может быть только в статусе Новая и Ожидает ответа.")

        if resolve_time_seconds and resolve_time_seconds <= 15:
            self.add_error('resolve_time_seconds', "Время на решение должно быть больше 15 сек.")