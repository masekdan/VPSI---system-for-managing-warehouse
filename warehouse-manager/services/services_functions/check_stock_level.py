def run(threshold=10, **kwargs):
    from database.models import Stocks
    for item in Stocks.objects.all():
        if item.quantity <= item.min_quantity:
            item.quantity = item.min_quantity + threshold  # Use argument if provided
            item.save()