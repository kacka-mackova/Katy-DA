# Pro zadanou proměnnou fruit_sales napiš kód, který vypočítá celkovou tržbu za ovoce.

fruit_sales = [
    {"fruit": "apple", "quantity": 30, "price_per_unit": 1.2},
    {"fruit": "orange", "quantity": 45, "price_per_unit": 0.8},
    {"fruit": "banana", "quantity": 25, "price_per_unit": 0.6},
    {"fruit": "grape", "quantity": 40, "price_per_unit": 2.5},
]


def revenue_of_fruits(revenue=0):
    total_revenue = 0
    for revenue in fruit_sales:
        total_revenue = revenue["quantity"] * revenue["price_per_unit"]
    return total_revenue


print(f"Celková tržba za ovoce je: {revenue_of_fruits(revenue=0)}")
