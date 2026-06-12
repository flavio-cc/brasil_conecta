# Brasil Conecta

Plataforma da comunidade brasileira no Canadá para descobrir serviços, produtos e grupos locais. Interface responsiva (desktop + mobile) construída com Django e Tailwind CSS.

## Stack

- **Backend:** Django 5 + SQLite
- **Frontend:** Tailwind CSS (CDN) + Plus Jakarta Sans
- **App principal:** `marketplace`

## Funcionalidades

- Hero com busca por serviço e cidade
- Categorias populares (Casa e reformas, Transporte, Beleza, Educação, Pets, Finanças, Produtos, Grupos)
- Posts em destaque com cards de prestadores (avaliação, verificado, WhatsApp)
- Produtos recentes com preço em CA$
- Grupos da comunidade
- Seed automático de dados de exemplo na primeira visita
- Navbar responsiva com links ativos e footer completo

## Rodar localmente

```bash
# Clone o repositório
git clone https://github.com/flavio-cc/brasil_conecta.git
cd brasil_conecta

# Crie e ative o ambiente virtual
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Instale as dependências
pip install django

# Crie as tabelas
python manage.py migrate

# Inicie o servidor
python manage.py runserver
```

Acesse: http://127.0.0.1:8000/

## Estrutura

```
brasil_conecta/
├── marketplace/
│   ├── models.py        # Category, ServiceProvider, Product, CommunityGroup
│   ├── views.py         # home view + seed automático
│   ├── urls.py
│   └── templates/
│       └── marketplace/
│           ├── base.html
│           └── home.html
└── brasil_conecta/
    ├── settings.py
    └── urls.py
```
