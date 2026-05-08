# 🏆 Sistema de Campeonato e Assistente Médico Web

## 📋 Descrição

Sistema web completo desenvolvido em **Django** para gerenciar campeonatos esportivos com integração de assistência médica. Projeto desenvolvido para a disciplina de **Novas Aplicações em Engenharia de Software** (1º Trimestre 2026).

### ✨ Características Principais

- ✅ **Gerenciamento de Campeonatos**: Criar, editar, visualizar e deletar campeonatos
- ✅ **Controle de Jogadores**: Cadastro e gerenciamento de jogadores por campus
- ✅ **Sistema de Inscrições**: Gerenciar inscrições de times com confirmação
- ✅ **Gestão de Jogos**: Registrar jogos, etapas e resultados
- ✅ **Módulo Médico**: Consultas, atendimentos e especialidades
- ✅ **Interface Responsiva**: Bootstrap 5 com design profissional
- ✅ **CRUD Completo**: CreateView, UpdateView, DeleteView, DetailView, ListView
- ✅ **Formulários Bonitos**: Django Crispy Forms + crispy-bootstrap5
- ✅ **Banco de Dados**: PostgreSQL via Neon.tech

---

## 🛠️ Tecnologias Utilizadas

| Componente | Tecnologia | Versão |
|-----------|-----------|--------|
| **Framework Web** | Django | 5.2.11 |
| **Linguagem** | Python | 3.12 |
| **Banco de Dados** | PostgreSQL | 15+ (Neon.tech) |
| **Frontend** | Bootstrap | 5.3.0 |
| **Formulários** | Django Crispy Forms | 2.4 |
| **Servidor** | Gunicorn | 21.2.0 |
| **Static Files** | WhiteNoise | 6.6.0 |

---

## 📁 Estrutura do Projeto

```
NovasAplicacoesEmEngSoftware/
├── config/                 # Configurações Django
│   ├── settings.py        # Settings (PostgreSQL, Crispy Forms)
│   ├── urls.py            # URLs principais
│   ├── wsgi.py            # WSGI app
│   └── asgi.py            # ASGI app
│
├── campeonato/            # App principal - CRUD completo
│   ├── models.py          # 10 modelos (Campus, Modalidade, Etapa, etc)
│   ├── views.py           # 50+ generic class-based views
│   ├── forms.py           # Formulários com Bootstrap styling
│   ├── urls.py            # URL routing
│   ├── admin.py           # Django Admin registrations
│   └── migrations/        # Database migrations
│
├── core/                  # App núcleo
│   ├── views.py           # Home e About (TemplateView)
│   ├── urls.py            # URLs core
│   └── templates/core/
│       ├── base.html      # Template base com herança
│       ├── index.html     # Homepage
│       └── sobre.html     # Página About
│
├── website/               # App website (placeholder)
│   ├── urls.py
│   └── views.py
│
├── templates/             # Templates globais
│   ├── base.html          # Template base (herança)
│   └── campeonato/        # Templates campeonato
│       ├── form.html      # Formulários
│       ├── detail.html    # Detalhes
│       ├── confirm_delete.html
│       └── [model]_list.html (9 templates)
│
├── static/                # Arquivos estáticos
│   ├── css/
│   │   ├── estilo.css     # CSS customizado
│   │   └── arena.css      # CSS alternativo
│   ├── js/                # JavaScript customizado
│   └── img/               # Imagens e diagramas
│
├── .env                   # Variáveis de ambiente
├── .gitignore            # Git ignore patterns
├── manage.py             # Django command utility
├── requirements.txt      # Python dependencies
└── venv/                 # Virtual environment (não commitado)
```

---

## 🏃 Quickstart

### 1️⃣ Pré-requisitos

- Python 3.12+
- pip (gerenciador de pacotes)
- Git
- PostgreSQL (ou Neon.tech account)

### 2️⃣ Instalação

```bash
# Clone o repositório
git clone <repository-url>
cd NovasAplicacoesEmEngSoftware

# Crie e ative o virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt
```

### 3️⃣ Configuração

```bash
# Configure as variáveis de ambiente
cp .env.example .env  # (ou configure manualmente)

# Edite o arquivo .env com suas credenciais:
# - SECRET_KEY
# - DATABASE_URL (Neon.tech)
# - ALLOWED_HOSTS
```

### 4️⃣ Banco de Dados

```bash
# Execute as migrações
python manage.py migrate

# Crie um superuser (admin)
python manage.py createsuperuser
```

### 5️⃣ Inicie o servidor

```bash
python manage.py runserver
```

Acesse: `http://localhost:8000`

**Admin**: `http://localhost:8000/admin`

---

## 📊 Modelos de Dados (10 Modelos)

### 1. **Campus**
- nome (CharField)
- Ordena: nome

### 2. **Modalidade**
- nome (CharField)
- Ordena: nome

### 3. **Etapa**
- nome (CharField)
- sequência (PositiveSmallIntegerField)
- quantidade_jogos (PositiveSmallIntegerField)

### 4. **Jogador**
- nome (CharField)
- id_jogador (CharField - unique)
- campus (ForeignKey → Campus)
- usuario (OneToOneField → User)
- atualizado_em, cadastrado_em (timestamps)

### 5. **Campeonato**
- nome (CharField)
- campus (ForeignKey)
- data (DateField)
- data_inscricao (DateTimeField)
- modalidades (ManyToManyField)
- cadastrado_por (ForeignKey → User)
- atualizado_em, cadastrado_em (timestamps)

### 6. **Inscrição**
- nome_time (CharField)
- jogadores (ManyToManyField → Jogador)
- campeonato (ForeignKey)
- modalidade (ForeignKey)
- confirmada (BooleanField)
- inscrito_por (ForeignKey → User)
- inscrito_em (DateTimeField)

### 7. **Jogo**
- time_1, time_2 (ForeignKey → Inscrição)
- data_hora (DateTimeField)
- etapa (ForeignKey)
- modalidade (ForeignKey)
- vencedor (ForeignKey)
- resultado (CharField)
- cadastrado_por (ForeignKey → User)
- atualizado_em, cadastrado_em (timestamps)

### 8. **Médico**
- nome (CharField)
- usuario (OneToOneField → User, nullable)

### 9. **Consulta**
- paciente (ForeignKey → Jogador)
- medico (ForeignKey)
- data (DateTimeField)
- criado_em (DateTimeField)

### 10. **Atendimento**
- consulta (ForeignKey)
- descricao (TextField)
- realizado (BooleanField)
- realizado_em (DateTimeField, nullable)

### Proxy Models
- **Paciente** (proxy de Jogador)
- **Especialidade** (proxy de Modalidade)

---

## 🚀 Views CRUD Implementadas (50+)

### Campus CRUD
- ✅ CampusListView
- ✅ CampusCreateView
- ✅ CampusDetailView
- ✅ CampusUpdateView
- ✅ CampusDeleteView

**Repetido para**: Modalidade, Etapa, Jogador, Campeonato, Inscrição, Jogo, Médico, Consulta, Atendimento

---

## 🎨 Templates e Herança

### Base Template (`base.html`)
- ✅ Navbar responsiva com dropdown menus
- ✅ Footer profissional
- ✅ Sistema de mensagens
- ✅ Bootstrap 5 grid
- ✅ Font Awesome icons
- ✅ Blocos extensíveis: `{% block content %}`, `{% block extra_css %}`, `{% block extra_js %}`

### Template Inheritance
```html
{% extends 'base.html' %}
{% block title %}Página{% endblock %}
{% block content %}
    <!-- Seu conteúdo -->
{% endblock %}
```

### Templates Disponíveis
- `base.html` - Template base (herança)
- `core/index.html` - Homepage com cards
- `core/sobre.html` - Página About com diagrama placeholders
- `campeonato/form.html` - Formulários com Crispy Forms
- `campeonato/detail.html` - Visualização de detalhes
- `campeonato/confirm_delete.html` - Confirmação de exclusão
- `campeonato/*_list.html` - Listas paginadas (9 templates)

---

## 🔑 Funcionalidades Implementadas

### ✅ CRUD Completo
- [x] CreateView com sucesso de mensagem
- [x] UpdateView com sucesso de mensagem
- [x] DeleteView com confirmação
- [x] DetailView com contexto customizado
- [x] ListView com paginação

### ✅ Formulários
- [x] Django Crispy Forms integrado
- [x] crispy-bootstrap5 styling
- [x] Validação automática
- [x] Widgets customizados

### ✅ Templates
- [x] Herança de template (base.html)
- [x] Blocos reutilizáveis
- [x] Responsividade Bootstrap 5
- [x] Navbar com dropdown
- [x] Cards e tabelas

### ✅ Banco de Dados
- [x] PostgreSQL via Neon.tech
- [x] 10+ modelos com relacionamentos
- [x] Migrations automáticas
- [x] Admin site configurado

### ✅ Organização
- [x] URLs estruturadas por app
- [x] Views organizadas com docstrings
- [x] Templates em diretórios apropriados
- [x] Static files estruturados
- [x] Settings com variáveis de ambiente

### ✅ Página Sobre
- [x] TemplateView implementada
- [x] Herança de base.html
- [x] Placeholders para diagramas
- [x] Descrição detalhada do projeto

---

## 📝 API Endpoints

### Campus
- GET `/campeonato/campus/` - Listar
- POST `/campeonato/campus/criar/` - Criar
- GET `/campeonato/campus/<id>/` - Detalhe
- POST `/campeonato/campus/<id>/editar/` - Editar
- POST `/campeonato/campus/<id>/deletar/` - Deletar

**Mesmo padrão para**: modalidade, etapa, jogador, campeonato, inscricao, jogo, medico, consulta, atendimento

---

## 🔐 Segurança

- ✅ CSRF protection ativo
- ✅ Secret key em variáveis de ambiente
- ✅ DEBUG = False em produção (recomendado)
- ✅ Senhas criptografadas
- ✅ SQL injection protection via ORM
- ✅ XSS protection automática

---

## 🚢 Deploy (Produção)

```bash
# Colete static files
python manage.py collectstatic --noinput

# Use Gunicorn como servidor
gunicorn config.wsgi:application

# Configure .env para produção
DEBUG=False
SECRET_KEY=seu-secret-key-super-seguro
ALLOWED_HOSTS=seu-dominio.com,www.seu-dominio.com
```

---

## 📚 Estrutura de URLs

```
/ → Home (index_view)
/sobre/ → Página About (SobreView)
/admin/ → Django Admin
/campeonato/ → App urls
  ├── campus/ → CampusListView
  ├── campus/criar/ → CampusCreateView
  ├── modalidade/ → ModalidadeListView
  ├── jogador/ → JogadorListView
  ├── campeonato/ → CampeonatoListView
  ├── inscricao/ → InscricaoListView
  ├── jogo/ → JogoListView
  ├── medico/ → MedicoListView
  ├── consulta/ → ConsultaListView
  └── atendimento/ → AtendimentoListView
/website/ → Website app (placeholder)
```

---

## 🧪 Testes

```bash
# Execute testes
python manage.py test

# Com coverage
coverage run --source='.' manage.py test
coverage report
```

---

## 📦 Dependências

Ver `requirements.txt` para a lista completa.

Principais:
- Django 5.2.11
- django-crispy-forms 2.4
- crispy-bootstrap5 2025.6
- psycopg2 (PostgreSQL driver)
- Pillow (imagens)
- python-dotenv

---

## 🐛 Troubleshooting

### Erro: "ModuleNotFoundError: django"
```bash
source venv/bin/activate  # Ative o venv
pip install -r requirements.txt
```

### Erro: "DATABASES não configurado"
```bash
# Verifique o arquivo .env
cat .env
# Configure DATABASE_URL corretamente
```

### Erro: "Migrations não aplicadas"
```bash
python manage.py migrate
```

### Servidor não inicia
```bash
python manage.py check  # Verifique erros
python manage.py collectstatic
```

---

## 📞 Suporte

Para questões sobre o projeto:
1. Verifique os logs do Django
2. Consulte a documentação do Django: https://docs.djangoproject.com
3. Verifique crispy-forms: https://django-crispy-forms.readthedocs.io

---

## 📄 Licença

Projeto educacional - 2026

---

## ✍️ Autor

Desenvolvido para a disciplina de **Novas Aplicações em Engenharia de Software**

Data: 08 de Maio de 2026

---

## 🎯 Requisitos Atendidos

- [x] Projeto Django funcional
- [x] PostgreSQL (Neon.tech)
- [x] Página "Sobre" com diagramas
- [x] Bootstrap 5 responsivo
- [x] Template inheritance (base.html)
- [x] Extra context / get_context_data
- [x] 10 models (sem contar User)
- [x] CRUD completo (Create, Read, Update, Delete)
- [x] Django Crispy Forms + crispy-bootstrap5
- [x] Organização correta de dirs
- [x] Todas as rotas e importações corretas
- [x] python manage.py runserver funciona
- [x] README.md profissional

