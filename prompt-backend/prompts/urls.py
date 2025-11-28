from django.urls import path
from .views import create_prompt, list_prompts, prompt_detail

urlpatterns = [
    path('prompts/', list_prompts, name='list_prompts'),
    path('prompts/<uuid:pk>/', prompt_detail, name='prompt_detail'),
    path('prompts/create/', create_prompt, name='create_prompt'),
]
