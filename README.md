# Brasil Conecta - Protótipo Django

Protótipo de portal para divulgação de prestadores de serviços, produtos e grupos da comunidade brasileira.

## Como rodar

```bash
cd brasil_conecta_django
python -m venv venv
source venv/bin/activate   # Mac/Linux
# ou: venv\Scripts\activate no Windows

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Acesse:
- Página inicial: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Estrutura

- `core/models.py`: categorias, serviços, produtos e grupos
- `core/views.py`: homepage e páginas simples
- `templates/core/home.html`: layout principal
- `static/core/css/styles.css`: design responsivo desktop/mobile

## Próximos passos sugeridos

- Adicionar cadastro/login de prestadores
- Upload real de imagens
- Busca por cidade/categoria
- Botão WhatsApp dinâmico
- Planos pagos: gratuito, destaque, profissional e empresa
