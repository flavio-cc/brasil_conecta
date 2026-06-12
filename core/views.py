from django.shortcuts import render
from .models import Category, ServiceProvider, Product, CommunityGroup

def seed_data():
    if Category.objects.exists():
        return

    categories = [
        ('Casa e reformas', '🏠', 124),
        ('Transporte', '🚗', 68),
        ('Saúde', '💚', 96),
        ('Beleza', '💅', 87),
        ('Educação', '🎓', 73),
        ('Pets', '🐾', 45),
        ('Finanças', '💰', 52),
        ('Produtos', '🛍️', 38),
    ]
    category_objs = []
    for name, icon, count in categories:
        category_objs.append(Category.objects.create(name=name, icon=icon, service_count=count))

    ServiceProvider.objects.create(
        category=category_objs[0],
        name='Brilho da Casa',
        description='Limpeza residencial e organização.',
        city='Longueuil',
        province='QC',
        whatsapp='15145550101',
        rating=5.0,
        review_count=32,
        verified=True,
        featured=True,
        image_url='https://images.unsplash.com/photo-1581578731548-c64695cc6952?auto=format&fit=crop&w=900&q=80'
    )
    ServiceProvider.objects.create(
        category=category_objs[3],
        name='Studio Beleza Brasil',
        description='Manicure, pedicure e design de sobrancelhas.',
        city='Montreal',
        province='QC',
        whatsapp='15145550102',
        rating=4.9,
        review_count=28,
        verified=True,
        featured=True,
        image_url='https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?auto=format&fit=crop&w=900&q=80'
    )
    ServiceProvider.objects.create(
        category=category_objs[0],
        name='Eletricista Oliveira',
        description='Instalações e reparos elétricos.',
        city='Brossard',
        province='QC',
        whatsapp='15145550103',
        rating=5.0,
        review_count=17,
        verified=True,
        featured=True,
        image_url='https://images.unsplash.com/photo-1621905252507-b35492cc74b4?auto=format&fit=crop&w=900&q=80'
    )
    ServiceProvider.objects.create(
        category=category_objs[4],
        name='Aulas de Português',
        description='Professora particular para crianças e adultos.',
        city='Laval',
        province='QC',
        whatsapp='15145550104',
        rating=4.9,
        review_count=21,
        verified=False,
        featured=True,
        image_url='https://images.unsplash.com/photo-1509062522246-3755977927d7?auto=format&fit=crop&w=900&q=80'
    )

    Product.objects.create(title='Bolos caseiros', price=45, city='Montreal', image_url='https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=900&q=80')
    Product.objects.create(title='Crochê personalizado', price=60, city='Longueuil', image_url='https://images.unsplash.com/photo-1618354691373-d851c5c3a990?auto=format&fit=crop&w=900&q=80')
    Product.objects.create(title='Kit skincare', price=75, city='Brossard', image_url='https://images.unsplash.com/photo-1556228720-195a672e8a03?auto=format&fit=crop&w=900&q=80')
    Product.objects.create(title='Brigadeiros gourmet', price=35, city='Laval', image_url='https://images.unsplash.com/photo-1606313564200-e75d5e30476c?auto=format&fit=crop&w=900&q=80')

    CommunityGroup.objects.create(name='Mães Brasileiras', city='Montreal', members=1286, icon='👩‍👧')
    CommunityGroup.objects.create(name='Brasileiros em Montreal', city='Montreal', members=982, icon='🇧🇷')
    CommunityGroup.objects.create(name='Homeschool Brasil Canadá', city='Canadá', members=756, icon='📚')
    CommunityGroup.objects.create(name='Empreendedores Brasileiros', city='Canadá', members=1431, icon='🚀')


def home(request):
    seed_data()
    context = {
        'categories': Category.objects.all()[:8],
        'services': ServiceProvider.objects.filter(featured=True)[:4],
        'products': Product.objects.all()[:4],
        'groups': CommunityGroup.objects.all()[:4],
    }
    return render(request, 'core/home.html', context)


def services(request):
    seed_data()
    return render(request, 'core/list.html', {'title': 'Serviços', 'items': ServiceProvider.objects.all()})


def products(request):
    seed_data()
    return render(request, 'core/list.html', {'title': 'Produtos', 'items': Product.objects.all()})


def groups(request):
    seed_data()
    return render(request, 'core/list.html', {'title': 'Grupos', 'items': CommunityGroup.objects.all()})
