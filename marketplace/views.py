from django.shortcuts import render
from .models import Category,ServiceProvider,Product,CommunityGroup

def seed_once():
    if Category.objects.exists(): return
    cats=[]
    for n,i,c in [('Casa e reformas','⌂','green-soft'),('Transporte','🚙','blue-soft'),('Beleza e bem-estar','🌷','pink-soft'),('Educação','🎓','blue-soft'),('Pets','🐾','yellow-soft'),('Finanças','$','green-soft'),('Produtos','▢','peach-soft'),('Grupos','👥','purple-soft')]:
        cats.append(Category.objects.create(name=n,icon=i,color_class=c))
    for cat,name,city,desc,rating,reviews,img in [
        (cats[0],'Limpeza Residencial','Toronto','Casa e reforr',5.0,32,'https://images.unsplash.com/photo-1581578731548-c64695cc6952?auto=format&fit=crop&w=800&q=80'),
        (cats[2],'Salão Beleza & Cia','Mississauga','Beleza e bem-estar',4.9,28,'https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?auto=format&fit=crop&w=800&q=80'),
        (cats[0],'Eletricista Profissional','Brampton','Casa e reformas',5.0,17,'https://images.unsplash.com/photo-1621905252507-b35492cc74b4?auto=format&fit=crop&w=800&q=80'),
        (cats[2],'Personal Trainer','Toronto','Saúde e bem-estar',4.9,21,'https://images.unsplash.com/photo-1571019613914-85f342c6a11e?auto=format&fit=crop&w=800&q=80')]:
        ServiceProvider.objects.create(category=cat,name=name,city=city,description=desc,rating=rating,reviews=reviews,image_url=img,whatsapp='14165550100')
    for title,sub,city,price,img in [
        ('Bolos Caseiros','Sólo encomenda','Toronto',45,'https://images.unsplash.com/photo-1563729784474-d77dbb933a9e?auto=format&fit=crop&w=800&q=80'),
        ('Sofá 3 lugares','Usado • Ótimo estado','Mississauga',350,'https://images.unsplash.com/photo-1555041469-a586c61ea9bc?auto=format&fit=crop&w=800&q=80'),
        ('Kit Skincare','Produtos importados','Toronto',75,'https://images.unsplash.com/photo-1556228720-195a672e8a03?auto=format&fit=crop&w=800&q=80'),
        ('Mesa de jantar','Madeira maciça','Brampton',420,'https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?auto=format&fit=crop&w=800&q=80')]:
        Product.objects.create(title=title,subtitle=sub,city=city,price=price,image_url=img)
    for name,city,members,icon,color in [('Mães Brasileiras','Toronto, ON','1.2k membros','👥','pink-soft'),('Brasileiros em Montreal','','890 membros','🌐','green-soft'),('Homeschool Brasil Canadá','','560 membros','📘','blue-soft'),('Empreendedores Brasileiros','','1.1k membros','💼','yellow-soft')]:
        CommunityGroup.objects.create(name=name,city=city,members_label=members,icon=icon,color_class=color)

def home(request):
    seed_once()
    return render(request,'marketplace/home.html',{'categories':Category.objects.all(),'services':ServiceProvider.objects.all(),'products':Product.objects.all(),'groups':CommunityGroup.objects.all()})
