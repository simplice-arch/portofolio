# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
import os


PORTFOLIO_DATA = {
    'profile': {
        'name': 'AKEY Gatiglo Simplice',
        'title': 'Étudiant en Développement Web · Backend & DevOps',
        'school': 'IAI-Togo — 2ᵉ année GLSI',
        'location': 'Lomé, Togo',
        'email': 'simpliceakey32@gmail.com',
        'whatsapp': '+228 79 80 73 45',
        'github': 'https://github.com/simplice-arch',
        'bio': (zzz
            "Passionné par le DevOps, l'automatisation et les technologies backend, "
            "je consacre une grande partie de mon temps à des projets concrets qui "
            "approfondissent mes connaissances en développement et en infrastructure. "
            "Mon objectif : évoluer vers un profil DevOps tout en conservant une solide "
            "expertise backend."
        ),
    },
    'skills': [
        {
            'category': 'Backend',
            'icon': '⚙️',
            'items': [
                {'name': 'Python',      'level': 85},
                {'name': 'Django',      'level': 80},
                {'name': 'API RESTful', 'level': 75},
                {'name': 'PostgreSQL',  'level': 70},
            ]
        },
        {
            'category': 'DevOps & Infra',
            'icon': '🚀',zzzzzzzzzzzzzzzzzzzzzzz
            'items': [
                {'name': 'Linux',          'level': 80},
                {'name': 'Git & GitHub',   'level': 85},
                {'name': 'Docker',         'level': 60},
                {'name': 'Automatisation', 'level': 75},
            ]
        },
        {
            'category': 'Intelligence Artificielle',
            'icon': '🤖',
            'items': [
                {'name': 'OpenAI API',     'level': 70},
                {'name': 'Gemini API',     'level': 65},
                {'name': 'Bots intelligents','level': 72},
                {'name': 'Intégration IA', 'level': 68},
            ]
        },
        {
            'category': 'Frontend',
            'icon': '🎨',
            'items': [
                {'name': 'HTML & CSS',         'level': 75},
                {'name': 'Tailwind CSS',        'level': 70},
                {'name': 'Django Templates',    'level': 80},
                {'name': 'JavaScript (bases)',  'level': 55},
            ]
        },
    ],
    'projects': [
        {
            'title': 'Gestionnaire de Projets (Jira-like)',
            'description': (
                'Application web de gestion de projets avec tableau Kanban, '
                'gestion des membres, priorisation des tâches et transitions de statut. '
                'Backend Django connecté à Supabase PostgreSQL.'
            ),
            'tags': ['Django', 'PostgreSQL', 'Supabase', 'Tailwind CSS'],
            'icon': '📋',
            'color': 'cyan',
            'github': '#',
        },
        {
            'title': 'Bot Intelligent IA',
            'description': (
                'Bot conversationnel intégrant les modèles OpenAI GPT et Google Gemini, '
                'capable de répondre à des questions complexes et d\'automatiser '
                'des flux de travail via des APIs tierces.'
            ),
            'tags': ['Python', 'OpenAI API', 'Gemini API', 'Automatisation'],
            'icon': '🤖',
            'color': 'violet',
            'github': '#',
        },
        {
            'title': 'API RESTful avec Django REST',
            'description': (
                'Conception et développement d\'une API RESTful complète avec '
                'authentification JWT, gestion des permissions et documentation Swagger. '
                'Déployée avec Docker.'
            ),
            'tags': ['Django REST', 'JWT', 'Docker', 'PostgreSQL'],
            'icon': '🔌',
            'color': 'emerald',
            'github': '#',
        },
        {
            'title': 'Automatisation Python',
            'description': (
                'Ensemble de scripts d\'automatisation pour la gestion de fichiers, '
                'scraping web et génération de rapports automatisés. '
                'Planification avec cron jobs sous Linux.'
            ),
            'tags': ['Python', 'Linux', 'Cron', 'Web Scraping'],
            'icon': '⚡',
            'color': 'amber',
            'github': '#',
        },
    ],
    'terminal_lines': [
        '$ whoami',
        'akey-simplice',
        '$ cat profile.json',
        '{',
        '  "role": "Backend & DevOps Engineer",',
        '  "location": "Lomé, Togo",',
        '  "stack": ["Python", "Django", "Docker", "Linux"],',
        '  "status": "Disponible pour stage"',
        '}',
        '$ echo "Bienvenue sur mon portfolio 🚀"',
        'Bienvenue sur mon portfolio 🚀',
    ],
}


def home(request):
    context = dict(PORTFOLIO_DATA)

    # Gestion formulaire de contact (POST)
    if request.method == 'POST':
        name    = request.POST.get('name', '').strip()
        email   = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and message:
            try:
                send_mail(
                    subject  = f'[Portfolio] {subject or "Message de contact"} — {name}',
                    message  = (
                        f"Nom    : {name}\n"
                        f"Email  : {email}\n\n"
                        f"Message:\n{message}"
                    ),
                    from_email   = settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL or 'simpliceakey32@gmail.com'],
                    fail_silently=False,
                )
                context['msg_success'] = True
            except Exception as e:
                context['msg_error'] = str(e)
        else:
            context['msg_error'] = 'Veuillez remplir tous les champs obligatoires.'

    return render(request, 'portfolio/home.html', context)


def download_cv(request):
    """Sert le CV PDF depuis /static/cv/cv.pdf"""
    import mimetypes
    from django.http import FileResponse, Http404

    cv_path = os.path.join(settings.BASE_DIR, 'static', 'cv', 'cv.pdf')
    if not os.path.exists(cv_path):
        raise Http404("CV non disponible pour l'instant.")
    return FileResponse(
        open(cv_path, 'rb'),
        content_type='application/pdf',
        as_attachment=True,
        filename='CV_AKEY_Gatiglo_Simplice.pdf',
    )
