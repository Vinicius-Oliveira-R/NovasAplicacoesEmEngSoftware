# CRITICAL ISSUES CHECKLIST & FIX GUIDE

**Project**: NovasAplicacoesEmEngSoftware  
**Analysis Date**: May 8, 2026  
**Total Issues Found**: 16  
**Critical Issues**: 4  
**High Priority Issues**: 6  
**Medium Priority Issues**: 6

---

## CRITICAL ISSUES (MUST FIX IMMEDIATELY)

### Issue #1: Missing App Registration in INSTALLED_APPS ⛔

**Location**: `config/settings.py` line 27-34

**Problem**:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',  # Only this one!
    # ❌ MISSING campeonato and website apps
]
```

**Impact**:
- Campeonato models won't work
- Website app won't be loaded
- Third-party packages won't function
- Migration system won't recognize campeonato migrations

**Fix**:
Add these lines to INSTALLED_APPS:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dal',                          # django-autocomplete-light
    'crispy_forms',                 # django-crispy-forms
    'crispy_bootstrap5',            # crispy-bootstrap5
    'django_extensions',            # django-extensions
    'django_filters',               # django-filter
    'debug_toolbar',                # django-debug-toolbar
    'core',                         # ← core app
    'campeonato',                   # ← ADD THIS
    'website',                      # ← ADD THIS
]
```

**Priority**: 🔴 **CRITICAL** - App won't work without this

---

### Issue #2: URL Routes Not Included in config/urls.py ⛔

**Location**: `config/urls.py` line 1-6

**Problem**:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
```

**Impact**:
- Campeonato URLs (60+ routes) are inaccessible
- Website URLs (3 routes) are inaccessible
- Users can't access championship management features

**Fix**:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('campeonato.urls')),    # ← ADD THIS
    path('', include('website.urls')),       # ← ADD THIS (optional: can use path('website/', ...))
]
```

Or with prefixes:
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('campeonato/', include('campeonato.urls')),
    path('website/', include('website.urls')),
]
```

**Priority**: 🔴 **CRITICAL** - Features unreachable

---

### Issue #3: Exposed Database Credentials ⛔

**Location**: `config/settings.py` line 73-88

**Problem**:
```python
database_url = 'postgresql://neondb_owner:npg_Mmr3KNoCXVD6@ep-holy-river-ac38q7p1-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': tmpPostgres.path.replace('/', ''),
        'USER': tmpPostgres.username,              # ❌ Exposed
        'PASSWORD': tmpPostgres.password,          # ❌ Exposed
        'HOST': tmpPostgres.hostname,
        'PORT': 5432,
        'OPTIONS': dict(parse_qsl(tmpPostgres.query)),
    }
}
```

**Impact**:
- Database password visible in source code
- Git history contains credentials
- Security breach if repository is public
- Unauthorized database access possible

**Fix**:
```python
import os
from dotenv import load_dotenv

load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'neondb'),
        'USER': os.getenv('DB_USER', 'neondb_owner'),
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

Create `.env` file (in project root):
```
DB_NAME=neondb
DB_USER=neondb_owner
DB_PASSWORD=npg_Mmr3KNoCXVD6
DB_HOST=ep-holy-river-ac38q7p1-pooler.sa-east-1.aws.neon.tech
DB_PORT=5432
DB_SSLMODE=require
DB_CHANNEL_BINDING=require
```

Add to `.gitignore`:
```
.env
*.env
```

Install: `pip install python-dotenv`

**Priority**: 🔴 **CRITICAL** - Security breach

---

### Issue #4: Exposed SECRET_KEY ⛔

**Location**: `config/settings.py` line 11

**Problem**:
```python
SECRET_KEY = 'django-insecure-@&3dm4&-hkw43^t-nwm@g9)r)ef+dryjem@zc#y1nibl&y$0b-'
```

**Impact**:
- Default insecure key
- Secret key visible in source code
- Session data could be compromised
- Cryptographic operations could be broken

**Fix**:
```python
SECRET_KEY = os.getenv('SECRET_KEY', 'change-me-in-production')

# Or generate a new one:
# from django.core.management.utils import get_random_secret_key
# SECRET_KEY = get_random_secret_key()
```

Add to `.env`:
```
SECRET_KEY=your-new-secret-key-here-change-in-production
```

Generate new key:
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

**Priority**: 🔴 **CRITICAL** - Security breach

---

## HIGH PRIORITY ISSUES (FIX SOON)

### Issue #5: No Admin Registration ⚠️

**Location**: 
- `campeonato/admin.py` - Empty
- `core/admin.py` - Empty
- `website/admin.py` - Empty

**Problem**:
```python
# campeonato/admin.py
from django.contrib import admin

# Register your models here.
# ← NO REGISTRATIONS
```

**Impact**:
- Django admin interface can't access any models
- Data management only through API/forms
- Admin has no visibility into database

**Fix** - `campeonato/admin.py`:
```python
from django.contrib import admin
from .models import (
    Campus, Modalidade, Etapa, Jogador, Campeonato,
    Inscricao, Jogo, Medico, Consulta, Atendimento,
    Paciente, Especialidade
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
    list_filter = ('sequencia',)

@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'id_jogador', 'campus')
    list_filter = ('campus',)
    search_fields = ('nome', 'id_jogador')

@admin.register(Campeonato)
class CampeonatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'campus', 'data')
    list_filter = ('campus', 'data')
    search_fields = ('nome',)

@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    list_display = ('nome_time', 'campeonato', 'confirmada')
    list_filter = ('confirmada', 'campeonato')
    search_fields = ('nome_time',)

@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):
    list_display = ('id', 'time_1', 'time_2', 'data_hora', 'vencedor')
    list_filter = ('etapa', 'modalidade', 'data_hora')
    search_fields = ('time_1__nome_time', 'time_2__nome_time')

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'medico', 'data')
    list_filter = ('data', 'medico')
    search_fields = ('paciente__nome',)

@admin.register(Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'consulta', 'realizado')
    list_filter = ('realizado',)

@admin.register(Paciente)
class PacienteAdmin(JogadorAdmin):
    pass

@admin.register(Especialidade)
class EspecialidadeAdmin(ModalidadeAdmin):
    pass
```

**Priority**: 🟡 **HIGH** - Admin access essential

---

### Issue #6: Incorrect Localization Settings ⚠️

**Location**: `config/settings.py` line 115-117

**Problem**:
```python
LANGUAGE_CODE = 'en-us'          # ❌ Should be Portuguese
TIME_ZONE = 'UTC'                # ❌ Should be Brazil timezone
USE_I18N = True
USE_TZ = True
```

**Impact**:
- UI in English instead of Portuguese
- Dates/times in UTC instead of local timezone
- Inconsistent with project purpose

**Fix**:
```python
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True
```

**Priority**: 🟡 **HIGH** - Localization important for Brazilian app

---

### Issue #7: Missing Static Files Configuration ⚠️

**Location**: `config/settings.py` line 121-122

**Problem**:
```python
STATIC_URL = 'static/'
# ❌ Missing STATIC_ROOT and STATIC_FILES_DIRS
```

**Impact**:
- Static files won't be collected for production
- CSS/JS may not load correctly

**Fix**:
```python
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

Then run:
```bash
python manage.py collectstatic
```

**Priority**: 🟡 **HIGH** - Production deployment needed

---

### Issue #8: DEBUG Mode Enabled ⚠️

**Location**: `config/settings.py` line 18

**Problem**:
```python
DEBUG = True  # ❌ Should be False in production
```

**Impact**:
- Detailed error pages expose sensitive information
- Secret information visible in stack traces
- Performance degradation

**Fix**:
```python
DEBUG = os.getenv('DEBUG', 'False') == 'True'
```

Add to `.env`:
```
DEBUG=False  # Or False for production
```

**Priority**: 🟡 **HIGH** - Security & performance

---

### Issue #9: Empty ALLOWED_HOSTS ⚠️

**Location**: `config/settings.py` line 21

**Problem**:
```python
ALLOWED_HOSTS = []  # ❌ Empty list
```

**Impact**:
- Only localhost can access in development
- Production deployment will fail with 400 error

**Fix**:
```python
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# Or for specific hosts:
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'yourdomain.com']
```

Add to `.env`:
```
ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com
```

**Priority**: 🟡 **HIGH** - Production deployment needed

---

## MEDIUM PRIORITY ISSUES

### Issue #10: Conflicting Settings Modules ⚠️

**Location**: `manage.py` line 7-8

**Problem**:
```python
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'naes2026.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')  # Overwrites first!
```

**Impact**:
- Confusing configuration
- Duplicate config directories
- Unclear which settings are active

**Fix**:
Keep only one:
```python
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
```

Remove unused `naes2026/` directory or properly document its purpose.

**Priority**: 🟠 **MEDIUM** - Code clarity

---

### Issue #11: No Custom Forms ⚠️

**Location**: Missing `forms.py` files in all apps

**Problem**:
Views use auto-generated forms:
```python
class CampusCreate(CreateView):
    fields = ['nome']  # Auto-generated form
```

**Impact**:
- No custom validation
- Limited form customization
- No help text or error messages
- Widget configuration limited

**Fix** - Create `campeonato/forms.py`:
```python
from django import forms
from .models import Campus, Jogador, Campeonato, Inscricao, Jogo

class CampusForm(forms.ModelForm):
    class Meta:
        model = Campus
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome do Campus'
            })
        }

class JogadorForm(forms.ModelForm):
    class Meta:
        model = Jogador
        fields = ['nome', 'id_jogador', 'campus', 'usuario']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'id_jogador': forms.TextInput(attrs={'class': 'form-control'}),
            'campus': forms.Select(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
        }

# ... more forms
```

Then update views:
```python
class CampusCreate(CreateView):
    model = Campus
    form_class = CampusForm  # Use custom form
    ...
```

**Priority**: 🟠 **MEDIUM** - UX improvement

---

### Issue #12: Views with Lazy Model Loading ⚠️

**Location**: `campeonato/views.py` lines ~480-500

**Problem**:
```python
class MedicoCreate(CreateView):
    model = None  # ❌ Set to None
    def get_model(self):
        from .models import Medico
        return Medico
    def get(self, request, *args, **kwargs):
        self.model = self.get_model()
        return super().get(request, *args, **kwargs)
    # ...
```

**Impact**:
- Workaround for circular import issues
- Code complexity
- Indicates design problems

**Fix**:
Consider extracting medical views to separate app or fixing imports:
```python
from .models import Medico, Consulta, Atendimento

class MedicoCreate(CreateView):
    model = Medico
    fields = ['nome', 'usuario']
    template_name = 'campeonato/form.html'
    success_url = reverse_lazy('medico-list')
    # ... normal implementation
```

**Priority**: 🟠 **MEDIUM** - Code quality

---

### Issue #13: Database Mismatch ⚠️

**Location**: Project root

**Problem**:
- `db.sqlite3` file exists
- Settings configured for PostgreSQL
- SQLite config commented out in settings

**Impact**:
- Confusion about which database is active
- Potential data inconsistency

**Fix**:
Choose one:
1. **Use PostgreSQL** (recommended):
   - Delete `db.sqlite3`
   - Keep current PostgreSQL configuration
   - Run migrations: `python manage.py migrate`

2. **Use SQLite** (development only):
   - Uncomment SQLite config in settings.py
   - Delete PostgreSQL config
   - Update requirements.txt

**Priority**: 🟠 **MEDIUM** - Configuration clarity

---

### Issue #14: Missing Template Base/Inheritance ⚠️

**Location**: `campeonato/templates/campeonato/form.html`

**Problem**:
All forms use single shared template without base template inheritance.

**Impact**:
- Code duplication across templates
- Inconsistent styling
- Difficult to make site-wide changes

**Fix**:
Create base template `campeonato/templates/base.html`:
```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Campeonato{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="/static/css/estilo.css">
    {% block extra_css %}{% endblock %}
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <!-- Navigation -->
    </nav>

    <main class="container mt-4">
        {% if messages %}
        <div class="alert alert-info alert-dismissible fade show" role="alert">
            {% for message in messages %}
                {{ message }}
            {% endfor %}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
        {% endif %}

        {% block content %}{% endblock %}
    </main>

    <footer class="mt-5 py-4 bg-light">
        <!-- Footer -->
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
```

**Priority**: 🟠 **MEDIUM** - Maintainability

---

### Issue #15: Incomplete Dependencies ⚠️

**Location**: `requirements.txt`

**Problem**:
Missing common production packages:
- `gunicorn` (WSGI server)
- `python-decouple` (env variable management)
- `whitenoise` (static file serving)

**Fix**:
```
django==5.2.11
django-autocomplete-light==3.12.1
django-braces==1.17.0
django-crispy-forms==2.4
crispy-bootstrap5==2025.6
django-debug-toolbar==6.1.0
django-extensions==4.1
django-filter==25.1
psycopg2==2.9.10
python-dateutil==2.9.0.post0
gunicorn==21.2.0
python-decouple==3.8
whitenoise==6.6.0
```

**Priority**: 🟠 **MEDIUM** - Production ready

---

### Issue #16: Missing .gitignore Configuration ⚠️

**Location**: `.gitignore` (if exists)

**Problem**:
May not have entries for:
- `.env` files
- `__pycache__/`
- `*.pyc`
- `db.sqlite3`
- `staticfiles/`
- Virtual environment

**Fix** - Complete `.gitignore`:
```
# Environment
.env
.env.local
.env.*.local

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
*.egg-info/
.eggs/

# Django
*.log
local_settings.py
db.sqlite3
/staticfiles/
/media/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Testing
.coverage
.pytest_cache/
htmlcov/
```

**Priority**: 🟠 **MEDIUM** - Repository hygiene

---

## SUMMARY BY PRIORITY

### 🔴 CRITICAL (Block deployment)
- [ ] Issue #1: Add campeonato and website to INSTALLED_APPS
- [ ] Issue #2: Include campeonato and website URLs
- [ ] Issue #3: Move database credentials to environment variables
- [ ] Issue #4: Move SECRET_KEY to environment variables

### 🟡 HIGH (Fix before using)
- [ ] Issue #5: Register models in admin
- [ ] Issue #6: Fix localization (pt-br, São Paulo timezone)
- [ ] Issue #7: Configure static files properly
- [ ] Issue #8: Move DEBUG setting to environment
- [ ] Issue #9: Configure ALLOWED_HOSTS

### 🟠 MEDIUM (Improve code quality)
- [ ] Issue #10: Resolve conflicting settings modules
- [ ] Issue #11: Create custom forms
- [ ] Issue #12: Resolve lazy model loading in views
- [ ] Issue #13: Decide on database and clean up
- [ ] Issue #14: Implement template inheritance
- [ ] Issue #15: Add missing dependencies
- [ ] Issue #16: Complete .gitignore

---

## RECOMMENDED IMPLEMENTATION ORDER

**Phase 1 (Immediate - 1-2 hours)**
1. Fix INSTALLED_APPS (Issue #1)
2. Fix URL routing (Issue #2)
3. Move credentials to .env (Issues #3, #4)
4. Register models in admin (Issue #5)

**Phase 2 (Today - 2-3 hours)**
5. Fix localization (Issue #6)
6. Configure static files (Issue #7)
7. Fix security settings (Issues #8, #9)
8. Resolve config conflicts (Issue #10)

**Phase 3 (This week - 5-6 hours)**
9. Create custom forms (Issue #11)
10. Clean up views (Issue #12)
11. Database cleanup (Issue #13)
12. Template refactoring (Issue #14)

**Phase 4 (This sprint - 3-4 hours)**
13. Update dependencies (Issue #15)
14. Complete .gitignore (Issue #16)
15. Testing and validation

**Total Time to Fix All Issues**: ~15-20 hours
