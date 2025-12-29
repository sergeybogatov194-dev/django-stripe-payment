import stripe
from django.conf import settings


stripe.api_key = settings.STRIPE_SECRET_KEY


def create_checkout_session(order):
    order_amount = int(order.total_cost_order * 100)
    order_amount_disc = int(order_amount - (order_amount * order.discount.percentage / 100))
    order_amount_tax = int(order_amount_disc + (order_amount_disc * order.tax.percentage / 100))
    line_items = [{
                "price_data": {
                    "currency": "usd",
                    "unit_amount": order_amount_tax,
                    "product_data": {
                        "name": f"Заказ №{order.id}",
                        "description": f"{order.count_items} items in order",
                    },
                },
                "quantity": 1,
            }]

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=line_items,
        mode="payment",
        success_url="http://localhost:8000/payments/success/?session_id={CHECKOUT_SESSION_ID}",
        cancel_url="http://localhost:8000/payments/cancel/",
    )
    return session