# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
import os


def home(request):
    context = {
        'profile': {
            'name': 'AKEY Gatiglo Simplice',
            'title': 'Etudiant en Developpement Web - Backend & DevOps',
            'school': 'IAI-Togo - 2e annee GLSI',
            'location': 'Lome, Togo',
            'email': 'simpliceakey32@gmail.com',
            'whatsapp': '+228 79 80 73 45',
            'github': 'https://github.com/simplice-arch',
        },
        'skills': [
            {
                'category': 'Backend',
                'icon': 'backend',
                'items': [
                    {'name': 'Python', 'level': 85},
                    {'name': 'Django', 'level': 80},
                    {'name': 'API RESTful', 'level': 75},
                    {'name': 'PostgreSQL', 'level': 70},
                ]
            },
            {
                'category': 'DevOps & Infra',
                'icon': 'devops',
                'items': [
                    {'name': 'Linux', 'level': 80},
                    {'name': 'Git & GitHub', 'level': 85},
                    {'name': 'Docker', 'level': 60},
                    {'name': 'Automatisation', 'level': 75},
                ]
            },
            {
                'category': 'Intelligence Artificielle',
                'icon': 'ai',
                'items': [
                    {'name': 'OpenAI API', 'level': 70},
                    {'name': 'Gemini API', 'level': 65},
                    {'name': 'Bots intelligents', 'level': 72},
                    {'name': 'Integration IA', 'level': 68},
                ]
            },
            {
                'category': 'Frontend',
                'icon': 'frontend',
                'items': [
                    {'name': 'HTML & CSS', 'level': 75},
                    {'name': 'Tailwind CSS', 'level': 70},
                    {'name': 'Django Templates', 'level': 80},
                    {'name': 'JavaScript', 'level': 55},
                ]
            },
        ],
        'projects': [
            {
                'title': 'Gestionnaire de Projets',
                'description': 'Application Kanban type Jira avec Django et Supabase PostgreSQL.',
                'tags': ['Django', 'PostgreSQL', 'Supabase', 'Tailwind'],
                'icon': 'P',
                'color': 'cyan',
                'github': 'https://github.com/simplice-arch',
            },
            {
                'title': 'Bot Intelligent IA',
                'description': 'Bot conversationnel integrant OpenAI GPT et Google Gemini.',
                'tags': ['Python', 'OpenAI', 'Gemini', 'Automatisation'],
                'icon': 'B',
                'color': 'violet',
                'github': 'https://github.com/simplice-arch',
            },
            {
                'title': 'API RESTful Django',
                'description': 'API complete avec JWT, permissions et documentation Swagger.',
                'tags': ['Django REST', 'JWT', 'Docker', 'PostgreSQL'],
                'icon': 'A',
                'color': 'emerald',
                'github': 'https://github.com/simplice-arch',
            },
            {
                'title': 'Automatisation Python',
                'description': 'Scripts de scraping, generation de rapports et cron jobs Linux.',
                'tags': ['Python', 'Linux', 'Cron', 'Scraping'],
                'icon': 'S',
                'color': 'amber',
                'github': 'https://github.com/simplice-arch',
            },
        ],
        'terminal_lines': [
            '$ whoami',
            'akey-simplice',
            '$ cat profile.json',
            '{',
            '  "role": "Backend & DevOps Engineer",',
            '  "location": "Lome, Togo",',
            '  "stack": ["Python", "Django", "Docker", "Linux"],',
            '  "status": "Disponible pour stage"',
            '}',
            '$ echo "Bienvenue sur mon portfolio"',
            'Bienvenue sur mon portfolio',
        ],
    }

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and message:
            try:
                send_mail(
                    subject='[Portfolio] ' + (subject or 'Message') + ' - ' + name,
                    message='Nom: ' + name + '\nEmail: ' + email + '\n\n' + message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=['simpliceakey32@gmail.com'],
                    fail_silently=False,
                )
                context['msg_success'] = True
            except Exception as e:
                context['msg_error'] = str(e)
        else:
            context['msg_error'] = 'Veuillez remplir tous les champs.'

    return render(request, 'portfolio/home.html', context)


def download_cv(request):
    from django.http import FileResponse, Http404
    cv_path = os.path.join(settings.BASE_DIR, 'static', 'cv', 'cv.pdf')
    if not os.path.exists(cv_path):
        raise Http404("CV non disponible.")
    return FileResponse(
        open(cv_path, 'rb'),
        content_type='application/pdf',
        as_attachment=True,
        filename='CV_AKEY_Gatiglo_Simplice.pdf',
    )