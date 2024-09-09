from .models import DiscountRule

def populate_discount_rules():
    discount_data = [
        {"consumer_type": "Residencial", "consumption_range": "<10000", "discount_value": 0.18, "cover_value": 0.90},
        {"consumer_type": "Residencial", "consumption_range": "10000-20000", "discount_value": 0.22, "cover_value": 0.95},
        {"consumer_type": "Residencial", "consumption_range": ">20000", "discount_value": 0.25, "cover_value": 0.99},
        {"consumer_type": "Comercial", "consumption_range": "<10000", "discount_value": 0.16, "cover_value": 0.90},
        {"consumer_type": "Comercial", "consumption_range": "10000-20000", "discount_value": 0.18, "cover_value": 0.95},
        {"consumer_type": "Comercial", "consumption_range": ">20000", "discount_value": 0.22, "cover_value": 0.99},
        {"consumer_type": "Industrial", "consumption_range": "<10000", "discount_value": 0.12, "cover_value": 0.90},
        {"consumer_type": "Industrial", "consumption_range": "10000-20000", "discount_value": 0.15, "cover_value": 0.95},
        {"consumer_type": "Industrial", "consumption_range": ">20000", "discount_value": 0.18, "cover_value": 0.99},
    ]

    for data in discount_data:
        rule = DiscountRule(**data)
        rule.save()

    print("Regras de desconto populadas com sucesso!")
