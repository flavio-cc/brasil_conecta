from django.shortcuts import render
from .models import Category, ServiceProvider, Product, CommunityGroup


def seed_data():
    CommunityGroup.objects.all().delete()
    Product.objects.all().delete()
    ServiceProvider.objects.all().delete()
    Category.objects.all().delete()

    categories = [
        ('Casa e reformas', '🏠', 124),
        ('Transporte', '🚗', 68),
        ('Beleza e bem-estar', '💅', 87),
        ('Educação', '🎓', 73),
        ('Pets', '🐾', 45),
        ('Finanças', '💰', 52),
        ('Produtos', '🛍️', 38),
        ('Grupos', '👥', 0),
    ]
    cats = [Category.objects.create(name=n, icon=i, service_count=c) for n, i, c in categories]
    # cats[0]=Casa, cats[1]=Transporte, cats[2]=Beleza, cats[3]=Educação, cats[4]=Pets, cats[5]=Finanças

    ServiceProvider.objects.create(
        category=cats[0], name='Limpeza Residencial',
        description='Limpeza residencial e organização profissional.',
        city='Toronto', province='ON', whatsapp='14165550101',
        rating=5.0, review_count=32, verified=True, featured=True,
        image_url='https://images.unsplash.com/photo-1581578731548-c64695cc6952?auto=format&fit=crop&w=900&q=80',
    )
    ServiceProvider.objects.create(
        category=cats[2], name='Salão Beleza & Cia',
        description='Manicure, pedicure e design de sobrancelhas.',
        city='Mississauga', province='ON', whatsapp='14165550102',
        rating=4.9, review_count=21, verified=True, featured=True,
        image_url='https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?auto=format&fit=crop&w=900&q=80',
    )
    ServiceProvider.objects.create(
        category=cats[0], name='Eletricista Profissional',
        description='Instalações e reparos elétricos residenciais e comerciais.',
        city='Brampton', province='ON', whatsapp='14165550103',
        rating=5.0, review_count=17, verified=True, featured=True,
        image_url='https://images.unsplash.com/photo-1621905252507-b35492cc74b4?auto=format&fit=crop&w=900&q=80',
    )
    ServiceProvider.objects.create(
        category=cats[2], name='Personal Trainer',
        description='Treinos personalizados para todos os níveis.',
        city='Markham', province='ON', whatsapp='14165550104',
        rating=4.9, review_count=21, verified=True, featured=True,
        image_url='https://images.unsplash.com/photo-1509062522246-3755977927d7?auto=format&fit=crop&w=900&q=80',
    )

    Product.objects.create(
        title='Bolos Caseiros', price=45, city='Toronto',
        image_url='https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=900&q=80',
    )
    Product.objects.create(
        title='Sofá 3 lugares', price=350, city='Mississauga',
        image_url='https://images.unsplash.com/photo-1555041469-a586c61ea9bc?auto=format&fit=crop&w=900&q=80',
    )
    Product.objects.create(
        title='Kit Skincare', price=75, city='Toronto',
        image_url='https://images.unsplash.com/photo-1556228720-195a672e8a03?auto=format&fit=crop&w=900&q=80',
    )
    Product.objects.create(
        title='Mesa de jantar', price=420, city='Brampton',
        image_url='https://images.unsplash.com/photo-1617806118233-18e1de247200?auto=format&fit=crop&w=900&q=80',
    )

    CommunityGroup.objects.create(name='Mães Brasileiras', city='Toronto, ON', members=1200, icon='👩‍👧')
    CommunityGroup.objects.create(name='Brasileiros em Montreal', city='Montreal, QC', members=890, icon='🇧🇷')
    CommunityGroup.objects.create(name='Homeschool Brasil Canadá', city='Canadá', members=560, icon='📚')
    CommunityGroup.objects.create(name='Empreendedores Brasileiros', city='Canadá', members=1100, icon='🚀')


def home(request):
    seed_data()
    context = {
        'categories': Category.objects.all()[:8],
        'services': ServiceProvider.objects.all()[:4],
        'products': Product.objects.all()[:4],
        'groups': CommunityGroup.objects.all()[:4],
    }
    return render(request, 'core/home.html', context)


def services(request):
    return render(request, 'core/list.html', {
        'title': 'Serviços',
        'items': ServiceProvider.objects.all(),
        'item_type': 'service',
    })


def products(request):
    return render(request, 'core/list.html', {
        'title': 'Produtos',
        'items': Product.objects.all(),
        'item_type': 'product',
    })


def groups(request):
    return render(request, 'core/list.html', {
        'title': 'Grupos da Comunidade',
        'items': CommunityGroup.objects.all(),
        'item_type': 'group',
    })
