from django.shortcuts import render, redirect,get_object_or_404
from .models import Category
from .forms import AddCategoryForm
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
    context = {'category': category}
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
