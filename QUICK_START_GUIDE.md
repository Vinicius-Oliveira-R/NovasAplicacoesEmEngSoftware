# QUICK START - FIX & RUN GUIDE

**Goal**: Get the Django project working immediately  
**Time**: ~30 minutes for critical fixes  
**Python Version**: 3.8+  
**Django Version**: 5.2.11

---

## 1. IMMEDIATE FIXES (Required for app to work)

### Step 1.1: Update `config/settings.py`

**Find this section:**
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]
```

**Replace with:**
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dal',
    'crispy_forms',
    'crispy_bootstrap5',
    'django_extensions',
    'django_filters',
    'debug_toolbar',
    'core',
    'campeonato',  # ← ADD THIS
    'website',     # ← ADD THIS
]
```

### Step 1.2: Update `config/urls.py`

**Current:**
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
```

**Replace with:**
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('campeonato.urls')),
    path('', include('website.urls')),
]
```

### Step 1.3: Create `.env` file in project root

**Create file**: `/path/to/project/.env`

```
# Database
DB_NAME=neondb
DB_USER=neondb_owner
DB_PASSWORD=npg_Mmr3KNoCXVD6
DB_HOST=ep-holy-river-ac38q7p1-pooler.sa-east-1.aws.neon.tech
DB_PORT=5432
DB_SSLMODE=require
DB_CHANNEL_BINDING=require

# Django
SECRET_KEY=django-insecure-@&3dm4&-hkw43^t-nwm@g9)r)ef+dryjem@zc#y1nibl&y$0b-
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Step 1.4: Update `config/settings.py` to use `.env`

**Add at the very top (after imports):**
```python
import os
from dotenv import load_dotenv

load_dotenv()
```

**Replace DATABASE section (lines 73-88) with:**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT', '5432'),
        'OPTIONS': {
            'sslmode': os.getenv('DB_SSLMODE', 'require'),
            'channel_binding': os.getenv('DB_CHANNEL_BINDING', 'require'),
        },
    }
}
```

**Update line 11 (SECRET_KEY):**
```python
SECRET_KEY = os.getenv('SECRET_KEY')
```

**Update line 18 (DEBUG):**
```python
DEBUG = os.getenv('DEBUG', 'False') == 'True'
```

**Update line 21 (ALLOWED_HOSTS):**
```python
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')
```

**Update localization (lines 115-117):**
```python
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
```

**Add static files configuration (after line 122):**
```python
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
```

### Step 1.5: Register Models in Admin

**Create/Update**: `campeonato/admin.py`

```python
from django.contrib import admin
from .models import (
    Campus, Modalidade, Etapa, Jogador, Campeonato,
    Inscricao, Jogo, Medico, Consulta, Atendimento
)

@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Modalidade)
class ModalidadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Etapa)
class EtapaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sequencia', 'quantidade_jogos')

@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'id_jogador', 'campus')
    search_fields = ('nome', 'id_jogador')

@admin.register(Campeonato)
class CampeonatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'campus', 'data')
    search_fields = ('nome',)

@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    list_display = ('nome_time', 'campeonato', 'confirmada')
    list_filter = ('confirmada',)

@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):
    list_display = ('id', 'data_hora', 'vencedor')
    list_filter = ('etapa', 'modalidade')

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'medico', 'data')
    list_filter = ('data',)

@admin.register(Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'consulta', 'realizado')
    list_filter = ('realizado',)
```

---

## 2. VERIFY YOUR INSTALLATION

Run these commands:

```bash
# Navigate to project directory
cd /path/to/NovasAplicacoesEmEngSoftware

# Check Python version
python --version  # Should be 3.8+

# Check Django version
python -m django --version  # Should be 5.2.11

# Test settings
python manage.py check  # Should report OK

# List installed apps
python manage.py shell -c "from django.conf import settings; print('\n'.join(settings.INSTALLED_APPS))"
```

---

## 3. INITIAL SETUP

### 3.1: Install Dependencies

```bash
# If not already installed
pip install -r requirements.txt

# Install python-dotenv (if not in requirements)
pip install python-dotenv
```

### 3.2: Run Migrations

```bash
# Apply all migrations
python manage.py migrate

# Check migration status
python manage.py showmigrations
```

### 3.3: Create Superuser

```bash
# Create admin user
python manage.py createsuperuser

# Follow prompts:
# Username: admin
# Email: admin@example.com
# Password: (create one)
```

### 3.4: Collect Static Files

```bash
python manage.py collectstatic --noinput
```

---

## 4. RUN THE SERVER

### Development Server

```bash
# Basic run
python manage.py runserver

# Or specify port
python manage.py runserver 8000

# Or allow external connections
python manage.py runserver 0.0.0.0:8000
```

**Access the app:**
- Homepage: `http://localhost:8000/`
- Admin: `http://localhost:8000/admin/`
- Campus list: `http://localhost:8000/listar/campus/`
- Modalidades: `http://localhost:8000/listar/modalidade/`

---

## 5. VERIFY EVERYTHING WORKS

### 5.1: Check Admin Panel

```
1. Go to http://localhost:8000/admin/
2. Login with your superuser credentials
3. You should see:
   - Campus
   - Modalidade
   - Etapa
   - Jogador
   - Campeonato
   - Inscricao
   - Jogo
   - Medico
   - Consulta
   - Atendimento
```

### 5.2: Check URLs

```
✓ http://localhost:8000/ (home)
✓ http://localhost:8000/listar/campus/ (list)
✓ http://localhost:8000/cadastrar/campus/ (create)
✓ http://localhost:8000/contato/ (website)
✓ http://localhost:8000/sobre/ (website)
```

### 5.3: Create Test Data

```bash
python manage.py shell

# In the shell:
from campeonato.models import Campus, Modalidade

# Create a campus
campus = Campus.objects.create(nome="Campus Principal")

# Create a modalidade
mod = Modalidade.objects.create(nome="LOL")

print("✓ Test data created successfully!")
```

---

## 6. TROUBLESHOOTING

### Issue: "No module named 'campeonato'"
**Solution**: Make sure you added 'campeonato' to INSTALLED_APPS

### Issue: "PostgreSQL connection error"
**Solution**: 
1. Check .env file has correct credentials
2. Ensure environment file is loaded: `load_dotenv()`
3. Test connection: `psql -h host -U user -d database`

### Issue: "No reverse match" URL error
**Solution**: Make sure all apps are in INSTALLED_APPS and URLs are included

### Issue: "OperationalError: relation does not exist"
**Solution**: Run migrations: `python manage.py migrate`

### Issue: "ModuleNotFoundError: No module named 'crispy_forms'"
**Solution**: Install requirements: `pip install -r requirements.txt`

### Issue: Static files not loading
**Solution**: 
1. Add to settings: `STATIC_ROOT = BASE_DIR / 'staticfiles'`
2. Run: `python manage.py collectstatic`

---

## 7. USEFUL DJANGO COMMANDS

```bash
# Create test data
python manage.py shell < commands.txt

# Check migrations
python manage.py showmigrations

# Create new migration
python manage.py makemigrations

# Rollback migration
python manage.py migrate campeonato 0003

# List all URLs
python manage.py show_urls

# Run Django shell
python manage.py shell

# Dump data to JSON
python manage.py dumpdata campeonato > backup.json

# Load data from JSON
python manage.py loaddata backup.json

# Clear database
python manage.py flush

# Generate SECRET_KEY
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## 8. PROJECT STATUS CHECKLIST

After making all fixes, verify:

- [ ] `config/settings.py` has all apps in INSTALLED_APPS
- [ ] `config/urls.py` includes all app URLs
- [ ] `.env` file exists with all credentials
- [ ] `load_dotenv()` is called in settings.py
- [ ] Admin models are registered
- [ ] Migrations are applied
- [ ] Superuser is created
- [ ] Server runs without errors
- [ ] Admin panel loads correctly
- [ ] Can access `/listar/campus/` URL
- [ ] Can create test data in admin panel

---

## 9. NEXT STEPS (AFTER BASIC SETUP)

1. **Create Custom Forms** (`campeonato/forms.py`)
   - Add validation
   - Add Bootstrap styling
   - Add help texts

2. **Create Base Template**
   - `campeonato/templates/base.html`
   - Inherit in all other templates

3. **Add Permissions**
   - User groups (Admin, Moderator, User)
   - View/edit/delete permissions

4. **Add Tests**
   - Model tests
   - View tests
   - URL tests

5. **Document API**
   - Add docstrings to views
   - Document admin actions

---

## EXPECTED PROJECT STRUCTURE (After Fixes)

```
NovasAplicacoesEmEngSoftware/
├── .env                    ✓ NEW
├── .gitignore              ✓ UPDATE
├── config/
│   ├── settings.py         ✓ FIXED
│   ├── urls.py             ✓ FIXED
│   ├── asgi.py
│   └── wsgi.py
├── campeonato/
│   ├── models.py           ✓ OK
│   ├── views.py            ✓ OK
│   ├── urls.py             ✓ OK (now included)
│   ├── admin.py            ✓ FIXED (now has registrations)
│   ├── forms.py            ✓ NEW (custom forms)
│   ├── migrations/
│   └── templates/campeonato/
├── core/
│   ├── models.py           ✓ OK (empty is fine)
│   ├── views.py            ✓ OK
│   ├── urls.py             ✓ OK
│   ├── admin.py            ✓ OK (empty is fine)
│   ├── migrations/
│   └── templates/core/
├── website/
│   ├── models.py           ✓ OK (empty is fine)
│   ├── views.py            ✓ OK
│   ├── urls.py             ✓ OK (now included)
│   ├── admin.py            ✓ OK (empty is fine)
│   ├── migrations/
│   └── templates/website/
├── static/
│   ├── css/
│   │   ├── arena.css
│   │   └── estilo.css
│   └── js/                 ← NEW
├── staticfiles/            ← NEW (after collectstatic)
├── media/                  ← NEW (for uploaded files)
├── manage.py               ✓ OK
├── requirements.txt        ✓ OK
└── PROJECT_STRUCTURE_ANALYSIS.md     ✓ Documentation
```

---

## TIME ESTIMATE

| Phase | Task | Time |
|-------|------|------|
| 1 | Update settings.py | 5 min |
| 2 | Update urls.py | 2 min |
| 3 | Create .env file | 3 min |
| 4 | Install dependencies | 2 min |
| 5 | Admin registration | 5 min |
| 6 | Run migrations | 2 min |
| 7 | Create superuser | 2 min |
| 8 | Test & verify | 5 min |
| **Total** | | **~30 min** |

---

## PRODUCTION CHECKLIST

Before deploying to production:

- [ ] Set `DEBUG = False`
- [ ] Change `SECRET_KEY` to a new value
- [ ] Configure `ALLOWED_HOSTS` with real domain
- [ ] Move database to production PostgreSQL
- [ ] Set `SECURE_SSL_REDIRECT = True`
- [ ] Set `SESSION_COOKIE_SECURE = True`
- [ ] Set `CSRF_COOKIE_SECURE = True`
- [ ] Configure email settings
- [ ] Set up proper logging
- [ ] Run security checks: `python manage.py check --deploy`
- [ ] Collect static files
- [ ] Set up backup strategy

---

**Last Updated**: May 8, 2026  
**Django Version**: 5.2.11  
**Python Version**: 3.8+
