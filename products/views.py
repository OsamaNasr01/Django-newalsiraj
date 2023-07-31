from django.shortcuts import render, redirect,get_object_or_404
from .models import Category, Product, Brand
from .forms import AddCategoryForm, AddProductForm, BrandForm
from django.contrib import messages

# Create your views here.

def p_category_list(request):
    categories = Category.objects.all()
    form = AddCategoryForm()
    return render(request, 'products/categories/p_category_list.html', {
        'categories':categories,
        'form': form,
        })



def add_p_category(request):
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('The Category has been Added Successfully!'))
            return redirect('p_category_list')
        else:
            errors = form.errors
            error_message = errors.as_text().split(':')[0]
            messages.error(request, ('There Was An Error adding the category' + error_message))
            return render(request, 'products/categories/add_p_category.html', {'form' : form, 'errors': errors})
    else:
        form = AddCategoryForm()
        return render(request, 'products/categories/add_p_category.html', {'form' : form})
    


def p_category_profile(request, slug):
    category = get_object_or_404(Category, slug=slug)
    form = AddProductForm()
    context = {
        'category': category,
        'products' : Product.objects.filter( category= category),
        'form' : form
        }
    return render(request, 'products/categories/p_category_profile.html', context)



def update_p_category(request, slug):
    category  = get_object_or_404(Category, slug=slug)
    if request.method == 'POST':
        form = AddCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, ('The Company Category has been Updated Successfully!'))
            return redirect('co_category_list')
    else:
        form = AddCategoryForm(instance=category)
    return render(request, 'products/categories/update_p_category.html', {
        'form': form,
        'category': category
        })


def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            category_id = request.POST.get('category_id')
            category = Category.objects.get(id=category_id)
            product.category = category
            product.save()
            messages.success(request, ('The Category has been Added Successfully!'))
            return redirect('p_category_list')
        else:
            errors = form.errors
            error_message = errors.as_text().split(':')[0]
            messages.error(request, ('There Was An Error adding the category' + error_message))
            return render(request, 'products/products/add_product.html', {'form' : form, 'errors': errors})
    else:
        form = AddProductForm()
        return render(request, 'products/products/add_product.html', {'form' : form})
    
def product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    form = AddProductForm(instance = product)
    context = {
        'product' : product,
        'form' : form
        }
    return render(request, 'products/products/product.html', context)


def update_product(request, slug):
    product  = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        form = AddProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, ('The Product Category has been Updated Successfully!'))
            return render(request, 'products/products/product.html', {'product':product})
    else:
        form = AddProductForm(instance=product)
    return render(request, 'products/products/update_product.html', {
        'form': form,
        'product': product
        })


def delete_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        product.delete()
        messages.success(request, ('The product has been Deleted Successfully!'))
        return redirect('p_category_list')


def brands(request):
    brands = Brand.objects.all()
    return render(request, 'products/brands/brands.html', {
        'brands': brands,
        'form' : BrandForm(),
    })


def add_brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('The Brand has been Added Successfully!'))
            return redirect('brands')
        else:
            errors = form.errors
            error_message = errors.as_text().split(':')[0]
            messages.error(request, ('There Was An Error adding the Brand' + error_message))
            return render(request, 'products/brands/add_brand.html', {'form' : form, 'errors': errors})
    else:
        form = BrandForm()
        return render(request, 'products/brands/add_brand.html', {'form' : form})
    

def brand_profile(request, slug):
    brand = get_object_or_404(Brand, slug=slug)
    return render(request, 'products/brands/brand_profile.html', {
        'brand': brand,
    })