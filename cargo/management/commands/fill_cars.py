from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        jj = [
            {"product_name": "lobster", "preview": "media/th.jpeg", "product_description": "moreplavaushie gadi",
             "category": Category(id=2),
             "price_per_unit": "5.5"},
            {"product_name": "lemon", "preview": "media/apelsin8.jpg", "product_description": "rastenie tropicheskoe",
             "category": Category(id=3),
             "price_per_unit": "4.5"},
            {"product_name": "onion", "preview": "media/th (1).jpeg", "product_description": "rastenie domashnee",
             "category": Category(id=3),
             "price_per_unit": "4.5"},
            {"product_name": "crab", "preview": "media/crab (2).jpeg",
             "product_description": "opyat moreplavaushie gadi", "category": Category(id=2),
             "price_per_unit": "4.5"},
        ]
        # products_list = []
        for j in jj:
            #     # category_list.append(**i)
            #     products_list.append(Product(product_name=j["product_name"], preview=j["preview"], category=j["category"], price_per_unit=j["price_per_unit"]))
            rec_2 = Car(product_name=j["product_name"], preview=j["preview"],
                            product_description=j["product_description"], category=j["category"],
                            price_per_unit=j["price_per_unit"])
            rec_2.save()
