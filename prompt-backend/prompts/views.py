# prompts/views.py
import json
from django.http import JsonResponse
from .models import Prompt
import redis

# Connect to Redis
r = redis.Redis(host='redis', port=6379, db=0)

def list_prompts(request):
    if request.method == "GET":
        prompts = Prompt.objects.all().order_by('-created_at')
        data = []
        for prompt in prompts:
            # Get view count from Redis
            view_count = r.get(f'prompt:{prompt.id}:views')
            data.append({
                'id': str(prompt.id),
                'title': prompt.title,
                'content': prompt.content,
                'complexity': prompt.complexity,
                'created_at': prompt.created_at.isoformat(),
                'view_count': int(view_count) if view_count else 0
            })
        return JsonResponse(data, safe=False)

def prompt_detail(request, pk):
    try:
        prompt = Prompt.objects.get(pk=pk)
    except Prompt.DoesNotExist:
        return JsonResponse({'error': 'Prompt not found'}, status=404)

    # Increment Redis counter
    r.incr(f'prompt:{prompt.id}:views')
    view_count = r.get(f'prompt:{prompt.id}:views')

    data = {
        'id': str(prompt.id),
        'title': prompt.title,
        'content': prompt.content,
        'complexity': prompt.complexity,
        'created_at': prompt.created_at.isoformat(),
        'view_count': int(view_count) if view_count else 0
    }
    return JsonResponse(data)

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import Prompt

@csrf_exempt
def create_prompt(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        prompt = Prompt.objects.create(
            title=data.get('title'),
            content=data.get('content'),
            complexity=data.get('complexity', 1)
        )
        return JsonResponse({
            'id': str(prompt.id),
            'title': prompt.title,
            'content': prompt.content,
            'complexity': prompt.complexity,
            'created_at': prompt.created_at.isoformat()
        })
    return JsonResponse({'error': 'Invalid method'}, status=405)
