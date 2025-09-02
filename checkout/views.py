from django.shortcuts import render, redirect
from .forms import CheckoutForm
from .models import Order, OrderItem
from cart.cart import Cart


def checkout(request):
    cart = Cart(request)
    if not len(cart):
        return redirect("cart:detail")

    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(**form.cleaned_data)
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product_name=item["product"].name,
                    price=item["price"],
                    quantity=item["quantity"],
                )
            cart.clear()
            return render(
                request, "checkout/checkout.html", {"order": order, "form": None}
            )
    else:
        form = CheckoutForm()

    return render(request, "checkout/checkout.html", {"form": form})
