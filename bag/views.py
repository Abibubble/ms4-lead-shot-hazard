from django.shortcuts import (
    render, redirect, get_object_or_404)
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """ A view to return the shopping bag """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of a product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(
                    request, f'Updated {size.upper()} {product.name} quantity'
                    + f' to {bag[item_id]["items_by_size"][size]}')
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request, f'Added size {size.upper()} {product.name} to'
                    + ' your bag')
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
                request, f'Added size {size.upper()} {product.name} to '
                + 'your bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)
