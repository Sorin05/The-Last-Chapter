from django.shortcuts import render

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in the bag")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51M30TDGQadtG99yWmSceHhL4k92mCtN0yy1mt1xhGNupAalnVLzLksbX4c1DcXiLtNgFqdXFezhZAzOYq79xNUrK00UkZJyo5g',

    }

    return render(request, template, context)
