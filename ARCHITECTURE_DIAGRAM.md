# Django Project Visual Architecture

## Current Project Structure

```
NovasAplicacoesEmEngSoftware/
│
├── config/                          # Main Django configuration
│   ├── settings.py                  ⚠️ ISSUES: Missing apps, exposed credentials
│   ├── urls.py                      ⚠️ INCOMPLETE: Only includes core.urls
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py                        ⚠️ CONFLICT: References multiple settings modules
│
├── campeonato/                      # Esports Championship + Medical Domain App
│   ├── models.py                    ✓ Complete models with migrations
│   ├── views.py                     ✓ Full CRUD views
│   ├── urls.py                      ✓ URL patterns defined but NOT INCLUDED
│   ├── admin.py                     ⚠️ EMPTY - No admin registration
│   ├── migrations/                  ✓ 4 migration files
│   └── templates/campeonato/
│       ├── form.html
│       ├── list/                    (10 templates)
│       └── detail/                  (10 templates)
│
├── core/                            # Base app (minimal)
│   ├── models.py                    ⚠️ EMPTY
│   ├── views.py                     ✓ Home and About views
│   ├── urls.py                      ✓ Only home route
│   ├── admin.py                     ⚠️ EMPTY
│   ├── migrations/
│   └── templates/core/
│       └── arquivo.html
│
├── website/                         # Website pages
│   ├── models.py                    ⚠️ EMPTY
│   ├── views.py                     ✓ Index, Contact, About views
│   ├── urls.py                      ✓ Routes defined but NOT INCLUDED
│   ├── admin.py                     ⚠️ EMPTY
│   ├── migrations/
│   └── templates/website/
│       ├── index.html
│       ├── contato.html
│       ├── sobre.html
│       └── (3 other templates)
│
├── naes2026/                        ⚠️ DUPLICATE CONFIG (not used)
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── static/
│   └── css/
│       ├── arena.css
│       └── estilo.css
│
├── db.sqlite3                       ⚠️ Commented out in settings
├── requirements.txt                 ✓ Defined
└── README.md


## Data Model Relationships

┌─────────────────────────────────────────────────────────┐
│          ESPORTS CHAMPIONSHIP DOMAIN                     │
└─────────────────────────────────────────────────────────┘

User (Django Auth)
 ├─ Jogador (1:1 OneToOneField)
 │  ├─ Campus (N:1 ForeignKey)
 │  └─ Consulta (1:N reverse relation)
 │
 ├─ Campeonato (1:N reverse - cadastrado_por)
 │  ├─ Campus (N:1 ForeignKey)
 │  ├─ Modalidade (N:M ManyToManyField)
 │  └─ Inscricao (1:N reverse)
 │
 ├─ Inscricao (1:N reverse - inscrito_por)
 │  ├─ Campeonato (N:1 ForeignKey)
 │  ├─ Modalidade (N:1 ForeignKey)
 │  ├─ Jogador (N:M via M2M)
 │  └─ Jogo (1:N as time_1, time_2, vencedor)
 │
 ├─ Jogo (1:N reverse - cadastrado_por)
 │  ├─ Inscricao (N:1 - time_1, time_2, vencedor)
 │  ├─ Etapa (N:1 ForeignKey)
 │  └─ Modalidade (N:1 ForeignKey)
 │
 ├─ Medico (1:1 OneToOne, nullable)
 │  └─ Consulta (1:N reverse)
 │
 └─ (Other fields)


┌─────────────────────────────────────────────────────────┐
│       MEDICAL CONSULTATION DOMAIN (Proxy)               │
└─────────────────────────────────────────────────────────┘

User (Django Auth)
 └─ Medico (1:1 OneToOneField, nullable)
    └─ Consulta (1:N reverse)
       ├─ Paciente (N:1 ForeignKey) ← Proxy for Jogador
       ├─ Medico (N:1 ForeignKey)
       └─ Atendimento (1:N reverse)
          ├─ Consulta (N:1 ForeignKey)
          └─ (attendance records)

Especialidade ← Proxy for Modalidade
 └─ (Same table as Modalidade)


## View CRUD Patterns

All views follow this pattern:

Create:    Campeonato (in route: cadastrar/) → form.html
Update:    Campeonato (in route: atualizar/) → form.html
Delete:    Campeonato (in route: excluir/)  → form.html
List:      Campeonato (in route: listar/)   → list/campeonato.html
Detail:    Campeonato (in route: detalhar/) → detail/campeonato.html

Applied to: Campus, Modalidade, Etapa, Jogador, Campeonato, 
            Inscricao, Jogo, Paciente, Especialidade, Medico,
            Consulta, Atendimento (13 models)


## URL Routing Diagram

┌─────────────────────────────────────────────────┐
│        config/urls.py                           │
│  path('', include('core.urls'))                 │
└─────────────────────────────────────────────────┘
         │
         ├─→ / (home)                             ✓ Working
         │
         ├─→ campeonato/urls.py                   ⚠️ NOT INCLUDED
         │   ├─ /cadastrar/campus/ → CREATE
         │   ├─ /listar/campus/ → LIST
         │   ├─ /detalhar/campus/<id>/ → DETAIL
         │   ├─ /atualizar/campus/<id>/ → UPDATE
         │   └─ ... (60+ routes, all defined)
         │
         └─→ website/urls.py                      ⚠️ NOT INCLUDED
             ├─ / → IndexView
             ├─ /contato/ → ContatoView
             └─ /sobre/ → SobreView


## Settings Configuration Issues

INSTALLED_APPS = [
    'django.contrib.admin',              ✓ Included
    'django.contrib.auth',               ✓ Included
    'django.contrib.contenttypes',       ✓ Included
    'django.contrib.sessions',           ✓ Included
    'django.contrib.messages',           ✓ Included
    'django.contrib.staticfiles',        ✓ Included
    'core',                              ✓ Included
    # ❌ MISSING:
    # 'campeonato',
    # 'website',
    # 'django_autocomplete_light',
    # 'crispy_forms',
    # 'crispy_bootstrap5',
    # 'django_extensions',
    # 'django_filters',
    # 'debug_toolbar',
]

DATABASE = {
    'default': {
        'ENGINE': 'postgresql',
        'NAME': 'neondb',                   ⚠️ Credentials exposed
        'USER': 'neondb_owner',             ⚠️ Credentials exposed
        'PASSWORD': '...',                  ⚠️ Credentials exposed
        'HOST': 'ep-holy-river-ac38q7p1...',
        'PORT': 5432,
    }
}

SECURITY SETTINGS:
- DEBUG = True                              ⚠️ Should be False in production
- SECRET_KEY = hardcoded/exposed           ⚠️ Should be environment variable
- ALLOWED_HOSTS = []                        ⚠️ Empty
- STATIC_ROOT = Not configured              ⚠️ Missing

LOCALIZATION:
- LANGUAGE_CODE = 'en-us'                   ⚠️ Should be 'pt-br'
- TIME_ZONE = 'UTC'                         ⚠️ Should be 'America/Sao_Paulo'


## Admin Interface Status

❌ NO MODELS REGISTERED

campeonato/admin.py:           Empty
core/admin.py:                 Empty
website/admin.py:              Empty

Required registrations:
□ Campus
□ Modalidade
□ Etapa
□ Jogador
□ Campeonato
□ Inscricao
□ Jogo
□ Medico
□ Consulta
□ Atendimento


## Forms Status

❌ NO CUSTOM FORMS DEFINED

All views use auto-generated forms:

views.py:
    fields = ['nome', 'id_jogador', 'campus', 'usuario']

Should have:
- forms.py with ModelForm classes
- Custom validation
- Widget customization
- Help text and error messages
