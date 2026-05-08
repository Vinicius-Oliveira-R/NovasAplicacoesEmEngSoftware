# 🚀 Como Usar o Projeto - Guia Rápido

## 📋 Índice
1. [Pré-requisitos](#pré-requisitos)
2. [Instalação Rápida](#instalação-rápida)
3. [Executar o Servidor](#executar-o-servidor)
4. [Acessar o Sistema](#acessar-o-sistema)
5. [Criar Dados de Teste](#criar-dados-de-teste)
6. [Troubleshooting](#troubleshooting)

---

## Pré-requisitos

- **Python**: 3.12+ (verifique com `python3 --version`)
- **Git**: para controle de versão
- **PostgreSQL**: Neon.tech (já configurado no .env)
- **pip**: gerenciador de pacotes Python

---

## Instalação Rápida

### 1. Clone o repositório
```bash
cd /home/vinicius/Documentos/FACULDADE/"Quarto ano Eng.Software"/NovasAplicacoesEmEngSoftware/NovasAplicacoesEmEngSoftware
```

### 2. Crie e ative o virtual environment
```bash
# Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

Se tiver erro de permissão, use:
```bash
pip install --user -r requirements.txt
```

---

## Executar o Servidor

### Inicie o servidor de desenvolvimento
```bash
source venv/bin/activate  # Se não estiver ativado
python manage.py runserver
```

Você verá:
```
Django version 5.2.11, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### Parar o servidor
Pressione `CTRL+C` no terminal

---

## Acessar o Sistema

### Páginas Principais

| URL | Descrição |
|-----|-----------|
| `http://localhost:8000/` | **Home** - Página inicial com cards |
| `http://localhost:8000/sobre/` | **Sobre** - Informações do projeto |
| `http://localhost:8000/admin/` | **Admin** - Painel administrativo |

### Módulos (Campeonato)

| URL | Descrição |
|-----|-----------|
| `http://localhost:8000/campeonato/campus/` | Listar Campus |
| `http://localhost:8000/campeonato/modalidade/` | Listar Modalidades |
| `http://localhost:8000/campeonato/etapa/` | Listar Etapas |
| `http://localhost:8000/campeonato/jogador/` | Listar Jogadores |
| `http://localhost:8000/campeonato/` | Listar Campeonatos |
| `http://localhost:8000/campeonato/inscricao/` | Listar Inscrições |
| `http://localhost:8000/campeonato/jogo/` | Listar Jogos |
| `http://localhost:8000/campeonato/medico/` | Listar Médicos |
| `http://localhost:8000/campeonato/consulta/` | Listar Consultas |
| `http://localhost:8000/campeonato/atendimento/` | Listar Atendimentos |

---

## Criar Dados de Teste

### 1. Acesse o Admin Panel
```
http://localhost:8000/admin/
```

### 2. Crie um usuário (se ainda não existe)
```bash
python manage.py createsuperuser
```

Siga os prompts:
```
Username: admin
Email: admin@example.com
Password: (digite uma senha forte)
```

### 3. Faça login no admin
- Abra `http://localhost:8000/admin/`
- Username: `admin`
- Password: (a senha que você definiu)

### 4. Crie dados de teste

#### Campus
1. Vá para Campus → Add Campus
2. Nome: "Campus A"
3. Clique Save

#### Modalidade
1. Vá para Modalidade → Add Modalidade
2. Nome: "LOL"
3. Clique Save

#### Etapa
1. Vá para Etapa → Add Etapa
2. Nome: "Final"
3. Sequência: 1
4. Quantidade de Jogos: 1
5. Clique Save

#### Jogador
1. Vá para Jogador → Add Jogador
2. Nome: "Jogador 1"
3. ID Jogador: "nick#1234"
4. Campus: "Campus A"
5. Usuário: (selecione admin)
6. Clique Save

#### Campeonato
1. Vá para Campeonato → Add Campeonato
2. Nome: "Campeonato 2026"
3. Campus: "Campus A"
4. Data: (escolha uma data)
5. Data de Inscrição: (escolha uma data)
6. Modalidades: (selecione "LOL")
7. Cadastrado por: admin
8. Clique Save

---

## Fluxo de Uso da Interface

### Para Gerenciar Campus
1. Acesse `http://localhost:8000/campeonato/campus/`
2. Clique **"+ Novo Campus"**
3. Preencha o formulário
4. Clique **"Salvar"**
5. Veja a lista com ações (Ver, Editar, Deletar)

### Padrão para Todas as Entidades
```
Lista → Novo → Preencher Formulário → Salvar → Ver/Editar/Deletar
```

---

## Comandos Django Úteis

### Verificar erros do projeto
```bash
python manage.py check
```

### Criar um usuário admin
```bash
python manage.py createsuperuser
```

### Executar migrations
```bash
python manage.py migrate
```

### Coletar static files (produção)
```bash
python manage.py collectstatic --noinput
```

### Shell interativo
```bash
python manage.py shell
```

### Limpar banco de dados (cuidado!)
```bash
python manage.py flush
```

---

## Estrutura de Pastas

```
NovasAplicacoesEmEngSoftware/
├── config/              # Configurações Django
├── campeonato/          # App principal
│   ├── models.py       # 10 modelos
│   ├── views.py        # 50+ views
│   ├── forms.py        # 10 formulários
│   ├── urls.py         # URLs
│   └── admin.py        # Admin customizado
├── core/                # App núcleo
│   ├── views.py        # Home e About
│   └── urls.py         # URLs
├── website/             # App website (placeholder)
├── templates/           # Templates HTML
│   ├── base.html       # Template base
│   ├── core/           # Templates core
│   └── campeonato/     # Templates campeonato
├── static/              # Arquivos estáticos
│   ├── css/            # Stylesheets
│   ├── js/             # JavaScript
│   └── img/            # Imagens
├── manage.py            # Django utility
├── requirements.txt     # Dependencies
├── .env                 # Variáveis de ambiente
└── venv/                # Virtual environment
```

---

## Troubleshooting

### Erro: "ModuleNotFoundError: No module named 'django'"
**Solução**: Ative o virtual environment
```bash
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

### Erro: "DATABASES não configurado"
**Solução**: Verifique o arquivo .env
```bash
cat .env
```

Certifique-se de que DATABASE_URL está correto.

### Erro: "Migrations não aplicadas"
**Solução**: Execute as migrations
```bash
python manage.py migrate
```

### Erro: "Port 8000 already in use"
**Solução**: Use outra porta
```bash
python manage.py runserver 8001
```

### Servidor não inicia
**Solução**: Verifique erros
```bash
python manage.py check
```

Corrija os erros mostrados e tente novamente.

### Página branca/sem estilo
**Solução 1**: Recarga a página (CTRL+F5)
**Solução 2**: Coletar static files
```bash
python manage.py collectstatic
```

---

## Dicas de Produção

### Desativar DEBUG
Edite `.env`:
```
DEBUG=False
```

### Usar Gunicorn
```bash
pip install gunicorn
gunicorn config.wsgi:application
```

### Configurar ALLOWED_HOSTS
Edite `.env`:
```
ALLOWED_HOSTS=seu-dominio.com,www.seu-dominio.com
```

---

## Suporte

Para mais informações:
- Leia [README.md](README.md)
- Consulte [IMPLEMENTACAO.md](IMPLEMENTACAO.md)
- Acesse a documentação do Django: https://docs.djangoproject.com

---

**Versão**: 1.0  
**Data**: 08 de Maio de 2026  
**Status**: ✅ Completo

