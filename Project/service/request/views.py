from django.shortcuts import render, redirect
from .models import Request
from .forms import RequestForm
from django.http import JsonResponse

def request_create_view(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['status'] != 'resolved':
                form.save()
            else:
                return JsonResponse({'error': "Заявка может быть только в статусе Новая и Ожидает ответа."}, status=400)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
        return JsonResponse({'success': True})

    form = RequestForm()
    requests = Request.objects.all()
    return render(request, 'request_create.html', {'form': form, 'requests': requests})

def get_requests_view(request):
    requests = list(Request.objects.values(
        'id', 'title', 'created_at', 'resolve_time_seconds', 'status'))
    return JsonResponse(requests, safe=False)