from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView

from diet.models import Product
from .forms import LoginForm, NewUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse


class StartPageView(View):
    def get(self, request):
        return render(request, template_name='base.html')


class UserLoginView(View):
    def get(self, request):
        form = LoginForm()
        ctx = {
            'form': form
        }
        return render(request, template_name='login_view.html', context=ctx)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('main'))
            return HttpResponse('no nie koniecznie')
        ctx = {
            'form': form
        }
        return render(request, template_name='base.html', context=ctx)


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('main'))


class NewUserView(View):
    def get(self, request):
        form = NewUserForm()
        ctx = {
            'form': form
        }
        return render(request, template_name='login_view.html', context=ctx)

    def post(self, request):
        form = NewUserForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            if User.objects.filter(username=login).exists():
                form.add_error('login', 'Taki login jest już zajęty')
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            if password != password2:
                form.add_error('password', 'hasła nie pasują do siebie')
            if not form.errors:
                email = form.cleaned_data['email']
                User.objects.create_user(login, email, password, first_name=first_name, last_name=last_name)
                return redirect(reverse('main'))
        ctx = {
            'form': form
        }
        return render(request, template_name='login_view.html', context=ctx)


class AddProductView(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('products')


class UpdateProductView(UpdateView):
    model = Product
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('products')


class ProductView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        cnx = {
            'product': product,
        }
        return render(request, template_name='product.html', context=cnx)


class ProductsView(View):

    def get(self, request):
        products = Product.objects.all()
        if self.request.GET.get('name'):
            products = products.filter(name__icontains=request.GET['name'])
        cnx = {
            'products': products
        }
        return render(request, template_name="products_list.html", context=cnx)
