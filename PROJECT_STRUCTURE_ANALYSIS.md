# Django Project Structure Analysis
**Date**: May 8, 2026  
**Project**: NovasAplicacoesEmEngSoftware  
**Analyzed**: Complete project structure, models, views, URLs, settings, templates, static files

---

## 1. PROJECT OVERVIEW

**Project Path**: `/home/vinicius/Documentos/FACULDADE/Quarto ano Eng.Software/NovasAplicacoesEmEngSoftware/NovasAplicacoesEmEngSoftware/`

**Django Version**: 5.2.11 (from requirements.txt)

**Project Purpose**: Esports championship management system with medical consultation domain overlay using proxy models

**Database**: PostgreSQL (Neon cloud database)

---

## 2. MODELS ANALYSIS

### 2.1 Campeonato App Models (`campeonato/models.py`)

**Domain Models (Esports Championship)**:
- **Campus** - Tournament campus/venue locations
  - Fields: `nome` (CharField)
  - Meta: Ordered by name, verbose plural "Campi"

- **Modalidade** - Game types/modes (LOL, CS, Fifa, etc.)
  - Fields: `nome` (CharField)
  - Meta: Ordered by name

- **Etapa** - Tournament stages/phases
  - Fields: `nome`, `sequencia` (stage order), `quantidade_jogos` (game count per stage)

- **Jogador** - Players in the tournament
  - Fields: `nome`, `id_jogador` (player ID), `campus` (FK), `atualizado_em`, `cadastrado_em`, `usuario` (OneToOne to User)

- **Campeonato** - Championship/Tournament
  - Fields: `nome`, `campus` (FK), `data`, `data_inscricao`, `modalidades` (M2M), `cadastrado_por` (FK to User), `atualizado_em`, `cadastrado_em`

- **Inscricao** - Team registrations for tournaments
  - Fields: `nome_time`, `jogadores` (M2M), `campeonato` (FK), `modalidade` (FK), `confirmada` (BooleanField), `confirmada_em`, `inscrito_em`, `inscrito_por` (FK)

- **Jogo** - Individual game matches
  - Fields: `time_1`, `time_2` (FK to Inscricao), `data_hora`, `etapa` (FK), `modalidade` (FK), `vencedor` (FK), `resultado`, `cadastrado_por` (FK), `atualizado_em`, `cadastrado_em`

**Medical Domain Models (Non-destructive proxy overlay)**:
- **Medico** - Medical doctors
  - Fields: `nome`, `usuario` (OneToOne to User, nullable)

- **Consulta** - Medical consultations
  - Fields: `paciente` (FK to Jogador), `medico` (FK), `data`, `criado_em`

- **Atendimento** - Medical attendance/treatment records
  - Fields: `consulta` (FK), `descricao` (TextField), `realizado` (BooleanField), `realizado_em`

**Proxy Models** (Domain terminology adapters):
- **Paciente** - Proxy for Jogador with "Paciente" terminology
  - Uses same database table as Jogador
  - Meta: verbose_name = "Paciente"

- **Especialidade** - Proxy for Modalidade with "Especialidade" terminology
  - Uses same database table as Modalidade
  - Meta: verbose_name = "Especialidade"

### 2.2 Core App Models (`core/models.py`)
**Status**: EMPTY - Only contains comment placeholder

### 2.3 Website App Models (`website/models.py`)
**Status**: EMPTY - Only contains comment placeholder

---

## 3. VIEWS STRUCTURE

### 3.1 Campeonato App Views (`campeonato/views.py`)

**CRUD Views Pattern**:
All models follow a standard CRUD pattern with Create, Read (List/Detail), Update, Delete views.

**Template Views for each model**:
- CampusCreate, CampusUpdate, CampusDelete, CampusList, CampusDetail
- ModalidadeCreate, ModalidadeUpdate, ModalidadeDelete, ModalidadeList, ModalidadeDetail
- EtapaCreate, EtapaUpdate, EtapaDelete, EtapaList, EtapaDetail
- JogadorCreate, JogadorUpdate, JogadorDelete, JogadorList, JogadorDetail
- CampeonatoCreate, CampeonatoUpdate, CampeonatoDelete, CampeonatoList, CampeonatoDetail
- InscricaoCreate, InscricaoUpdate, InscricaoDelete, InscricaoList, InscricaoDetail
- JogoCreate, JogoUpdate, JogoDelete, JogoList, JogoDetail

**Medical Domain Views** (using proxy models):
- PacienteCreate, PacienteUpdate, PacienteDelete, PacienteList, PacienteDetail
- EspecialidadeCreate, EspecialidadeUpdate, EspecialidadeDelete, EspecialidadeList, EspecialidadeDetail
- MedicoCreate, MedicoUpdate, MedicoDelete, MedicoList, MedicoDetail
- ConsultaCreate, ConsultaList, ConsultaDetail
- AtendimentoCreate, AtendimentoList, AtendimentoDetail

**View Implementation Details**:
- Uses Django generic class-based views (CreateView, UpdateView, DeleteView, ListView, DetailView)
- Template: All forms use `campeonato/form.html` (single shared template)
- Context: All views pass `titulo` and `botao` in `extra_context`
- Medical views have workarounds for lazy model loading (circular import prevention)

### 3.2 Core App Views (`core/views.py`)
```python
def home(request):
    return render(request, 'core/arquivo.html')

class SobreView(TemplateView):
    template_name = 'core/AssistenteWeb/index.html'
```

### 3.3 Website App Views (`website/views.py`)
- **IndexView** - TemplateView for `website/index.html`
- **ContatoView** - TemplateView for `website/contato.html`
- **SobreView** - TemplateView for `website/sobre.html`

---

## 4. URL ROUTING CONFIGURATION

### 4.1 Root URL Configuration (`config/urls.py`)
```python
urlpatterns = [
    path('', include('core.urls')),
]
```
⚠️ **Issue**: Admin URL not included, but Django admin should be auto-available

### 4.2 Core App URLs (`core/urls.py`)
```python
urlpatterns = [
    path('', home, name='home'),
]
```

### 4.3 Campeonato App URLs (`campeonato/urls.py`)
**Comprehensive URL patterns for all CRUD operations**:

**Campus routes**: 
- `cadastrar/campus/` → CampusCreate (name: `campus-create`)
- `atualizar/campus/<id>/` → CampusUpdate (name: `campus-update`)
- `excluir/campus/<id>/` → CampusDelete (name: `campus-delete`)
- `listar/campus/` → CampusList (name: `campus-list`)
- `detalhar/campus/<id>/` → CampusDetail (name: `campus-detail`)

**Modalidade routes**: Similar pattern as Campus + Especialidade proxy routes

**Etapa routes**: Similar CRUD pattern

**Jogador routes**: Similar CRUD pattern + Paciente proxy routes

**Tournament/Match routes**: Campeonato, Inscricao, Jogo - all with CRUD patterns

**Medical routes**:
- Médico (Create, List, Detail only - no Update/Delete)
- Consulta (Create, List, Detail only)
- Atendimento (Create, List, Detail only)

**URL Naming Convention**: `{entity}-{action}` (e.g., `jogador-create`, `campeonato-list`)

### 4.4 Website App URLs (`website/urls.py`)
```python
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("contato/", ContatoView.as_view(), name="contato"),
    path("sobre/", SobreView.as_view(), name="sobre"),
]
```

⚠️ **Issues Found**:
1. **Missing root include**: campeonato and website apps are NOT included in config/urls.py
2. **URL routing conflict**: Only core.urls is included as root
3. **Orphaned URLs**: campeonato/urls.py and website/urls.py exist but are not referenced

---

## 5. SETTINGS CONFIGURATION (`config/settings.py`)

### 5.1 Basic Settings
- **DEBUG**: True (SECURITY WARNING - for production)
- **SECRET_KEY**: Hardcoded (SECURITY WARNING - exposed)
- **ALLOWED_HOSTS**: Empty list (SECURITY WARNING)
- **LANGUAGE_CODE**: 'en-us' (should be 'pt-br' for Brazilian Portuguese)
- **TIME_ZONE**: 'UTC' (should be 'America/Sao_Paulo' or '*America/Sao_Paulo*' - unusual format)

### 5.2 Installed Apps (INCOMPLETE)
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',  # ✓ Core app registered
]
```

⚠️ **CRITICAL ISSUE**: 
- ❌ `campeonato` NOT registered
- ❌ `website` NOT registered
- ❌ Multiple third-party packages in requirements.txt NOT registered:
  - django-autocomplete-light
  - django-braces
  - django-crispy-forms
  - crispy-bootstrap5
  - django-debug-toolbar
  - django-extensions
  - django-filter

### 5.3 Database Configuration
**Current**: PostgreSQL (Neon cloud)
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'neondb',
        'USER': 'neondb_owner',
        'PASSWORD': 'npg_Mmr3KNoCXVD6',  # EXPOSED - SECURITY WARNING
        'HOST': 'ep-holy-river-ac38q7p1-pooler.sa-east-1.aws.neon.tech',
        'PORT': 5432,
        'OPTIONS': {'sslmode': 'require', 'channel_binding': 'require'},
    }
}
```

⚠️ **SECURITY ISSUES**:
1. Database credentials hardcoded in settings
2. Password visible in source code
3. Uses Neon PostgreSQL (cloud) in development

### 5.4 Middleware
Standard Django middleware configured:
- SecurityMiddleware
- SessionMiddleware
- CommonMiddleware
- CsrfViewMiddleware
- AuthenticationMiddleware
- MessageMiddleware
- XFrameOptionsMiddleware

### 5.5 Templates
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # No global template directories
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### 5.6 Static Files
```python
STATIC_URL = 'static/'
STATIC_ROOT = Not configured (should be set)
```

---

## 6. REQUIREMENTS AND DEPENDENCIES

### 6.1 Requirements.txt
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
```

**Package Analysis**:
- ✓ Django 5.2.11 (latest)
- ✓ PostgreSQL support (psycopg2)
- ✓ Form handling (crispy-forms with Bootstrap5)
- ✓ Development tools (debug-toolbar, extensions)
- ✓ Admin enhancements (autocomplete-light, braces)
- ✓ Filtering (django-filter)

---

## 7. TEMPLATES STRUCTURE

### 7.1 Template Directories

**Campeonato App Templates** (`campeonato/templates/campeonato/`):
- `form.html` - Shared form template for all CRUD create/update/delete operations
- `list/` directory:
  - `atendimento.html`
  - `campeonato.html`
  - `campus.html`
  - `consulta.html`
  - `etapa.html`
  - `inscricao.html`
  - `jogador.html`
  - `jogo.html`
  - `medico.html`
  - `modalidade.html`
- `detail/` directory:
  - `atendimento.html`
  - `campeonato.html`
  - `campus.html`
  - `consulta.html`
  - `etapa.html`
  - `inscricao.html`
  - `jogador.html`
  - `jogo.html`
  - `medico.html`
  - `modalidade.html`

**Core App Templates** (`core/templates/core/`):
- `arquivo.html` - Home page template

**Website App Templates** (`website/templates/website/`):
- `contato.html` - Contact page
- `exemplo.html` - Example page
- `index.html` - Homepage
- `modelo.html` - Template model
- `modelo2.html` - Alternative template model
- `sobre.html` - About page

### 7.2 Template Issues
⚠️ **Issues**:
1. No base template inheritance setup visible
2. Single shared `form.html` for all forms (reuse pattern unclear)
3. Template context relies on `titulo` and `botao` variables
4. No template fragments or includes visible

---

## 8. STATIC FILES STRUCTURE

### 8.1 Static Files (`static/`)
```
static/
├── css/
│   ├── arena.css
│   └── estilo.css
```

**CSS Files**:
- `arena.css` - Arena/championship styling
- `estilo.css` - General styling

⚠️ **Issue**: 
- STATIC_ROOT not configured in settings
- No JavaScript files present
- Minimal CSS setup

---

## 9. ADMIN CONFIGURATION

### 9.1 Admin Registration Status
⚠️ **CRITICAL**: All admin.py files are EMPTY:
- `campeonato/admin.py` - EMPTY (only comment)
- `core/admin.py` - EMPTY (only comment)
- `website/admin.py` - EMPTY (only comment)

**Impact**: NO models are registered in Django admin interface

---

## 10. FORMS

⚠️ **Status**: NO forms.py files exist in any app

All views use Django's auto-generated forms from model fields specified in views:
```python
fields = ['nome', 'id_jogador', 'campus', 'usuario']  # Model fields
```

---

## 11. MIGRATION STATUS

### 11.1 Campeonato App Migrations
```
migrations/
├── 0001_initial.py
├── 0002_alter_campus_options_alter_modalidade_options.py
├── 0003_especialidade_paciente.py
├── 0004_medico_consulta_atendimento.py
```

**Migration History**:
1. Initial model creation
2. Modified Campus and Modalidade Meta options
3. Added Especialidade and Paciente proxy models
4. Added medical models (Medico, Consulta, Atendimento)

### 11.2 Other App Migrations
- Core: Only empty `__init__.py` (no migrations)
- Website: Only empty `__init__.py` (no migrations)

---

## 12. ALTERNATIVE CONFIG DIRECTORY

### 12.1 `naes2026/` Directory
Located at same level as `config/`:
- `__init__.py`
- `asgi.py`
- `settings.py`
- `urls.py`
- `wsgi.py`

⚠️ **Issue**: DUPLICATE project configuration
- manage.py attempts to use BOTH `naes2026.settings` and `config.settings`
- Only one should be active

---

## 13. OTHER PROJECT FILES

- `db.sqlite3` - SQLite database (commented out in settings, but file exists)
- `manage.py` - Django management command (has conflicting settings)
- `comandos.txt` - Command documentation/notes
- `laboratorio.txt` - Lab notes/documentation
- `github.py` - GitHub integration script (purpose unclear)
- `prompt_template.txt` - Template for prompts (likely for AI/LLM)

---

## 14. IDENTIFIED ISSUES AND PROBLEMS

### 🔴 **CRITICAL ISSUES**

1. **Missing App Registration** (config/settings.py):
   - `campeonato` app not in INSTALLED_APPS → Models won't work
   - `website` app not in INSTALLED_APPS
   - Third-party packages listed in requirements but NOT in INSTALLED_APPS

2. **Broken URL Routing** (config/urls.py):
   - Only `core.urls` included
   - `campeonato.urls` - created but never included
   - `website.urls` - created but never included
   - No admin URL path

3. **Exposed Credentials** (config/settings.py):
   - Database password visible in source code
   - SECRET_KEY exposed and using default Django insecure key
   - Should use environment variables

4. **Views with Lazy Model Loading** (campeonato/views.py):
   - MedicoCreate, MedicoDelete, ConsultaCreate use workarounds
   - Indicates circular import issues or model organization problems

### 🟡 **HIGH PRIORITY ISSUES**

5. **Empty Admin Registration**:
   - No models registered in admin.py files
   - Admin interface will have no access to data

6. **Incomplete Settings**:
   - ALLOWED_HOSTS empty
   - DEBUG=True in production
   - No STATIC_ROOT path configured
   - Wrong LANGUAGE_CODE ('en-us' instead of 'pt-br')
   - Unusual TIME_ZONE format

7. **No Custom Forms**:
   - All forms auto-generated from model fields
   - No validation beyond Django defaults
   - No form customization possible

8. **Duplicate Config** (manage.py):
   - References both `naes2026` and `config` settings modules
   - Unclear which is active

### 🟠 **MEDIUM PRIORITY ISSUES**

9. **Template Structure**:
   - No base template for inheritance
   - Single `form.html` shared by all forms
   - Missing CSS/JS organization

10. **Database Mismatch**:
    - `db.sqlite3` exists but settings use PostgreSQL
    - Commented SQLite config in settings.py

11. **Static Files**:
    - STATIC_ROOT not configured
    - Only CSS, no JS files

---

## 15. ARCHITECTURE OBSERVATIONS

### 15.1 Design Patterns
- **Domain-Driven Design Attempt**: Using proxy models to overlay medical domain on sports domain
- **Generic Class-Based Views**: Consistent use of Django CBVs for CRUD operations
- **Template Reuse**: Single `form.html` for all create/update/delete operations

### 15.2 Mixed Domains
- **Primary Domain**: Esports championship management (Campus, Jogador, Jogo, etc.)
- **Secondary Domain**: Medical consultation system (Medico, Consulta, Atendimento, Paciente)
- **Implementation**: Non-destructive using proxy models

### 15.3 Code Organization
- **Monolithic Campeonato App**: Contains all CRUD views for both domains
- **Minimal Core/Website**: Mostly template views, no models or complex logic

---

## 16. RECOMMENDATIONS FOR RESTRUCTURING

### Phase 1: Fix Critical Issues
1. ✅ Add missing apps to INSTALLED_APPS
2. ✅ Add third-party packages to INSTALLED_APPS
3. ✅ Include campeonato and website URLs in config/urls.py
4. ✅ Move credentials to environment variables
5. ✅ Register models in admin.py

### Phase 2: Code Organization
1. Extract medical views to separate medical app
2. Create custom forms.py for validation
3. Implement template inheritance and base template
4. Resolve circular import issues in views

### Phase 3: Configuration
1. Set STATIC_ROOT and STATIC_FILES_DIRS
2. Fix LANGUAGE_CODE and TIME_ZONE
3. Configure security settings for production
4. Remove or clean up naes2026 config duplicate

### Phase 4: Enhancement
1. Add proper error handling and validation
2. Implement permissions and authentication
3. Add tests
4. Optimize database queries

---

## SUMMARY

**Current State**: Functional but incomplete Django application with:
- ✓ Working models and migrations
- ✓ Basic CRUD views implemented
- ✓ URL routing defined (but not fully integrated)
- ✓ PostgreSQL database configured
- ✗ Missing app registration
- ✗ Missing admin setup
- ✗ Missing URL integration
- ✗ Security issues with exposed credentials
- ✗ No custom forms
- ✗ Incomplete settings configuration

**Restructuring Priority**: HIGH - Multiple critical issues must be addressed before production deployment.
