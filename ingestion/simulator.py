import copy
import random
from datetime import datetime


import copy
import random
from datetime import datetime

def simulate_products(products):
    simulated_products=copy.deepcopy(products)
    for product in simulated_products:
        if random.random()<0.30:
            percentage=random.randint(-10,15)
            product["price"]=round(product["price"]*(1+percentage/100),2)
        if random.random()<0.40:
            product["stock"]+=random.randint(-5,20)
            if product["stock"]<0:
                product["stock"]=0
        if random.random()<0.15:
            rating=product["rating"]+random.uniform(-0.5,0.5)
            rating=max(0,min(5,rating))
            product["rating"]=round(rating,2)
        if random.random()<0.20:
            discount=product["discountPercentage"]+random.uniform(-2,2)
            discount=max(0,discount)
            product["discountPercentage"]=round(discount,2)
        product["ingestion_timestamp"]=datetime.utcnow().isoformat()
    return simulated_products


def simulate_users(users):
    simulated_users=copy.deepcopy(users)
    timestamp=datetime.utcnow().isoformat()

    for user in simulated_users:
        user["ingestion_timestamp"]=timestamp

    return simulated_users

def simulate_carts(carts):
    simulated_carts=copy.deepcopy(carts)
    for cart in simulated_carts:
        if random.random()<0.30:
            cart["totalQuantity"]+=random.randint(-2,5)
            if cart["totalQuantity"]<0:
                cart["totalQuantity"]=0
        if random.random()<0.25:
            cart["discountedTotal"]+=random.randint(-100,200)
            if cart["discountedTotal"]<0:
                cart["discountedTotal"]=0
        cart["ingestion_timestamp"]=datetime.utcnow().isoformat()
    return simulated_carts


def simulate_all(data):

    data["products"] = simulate_products(
        data["products"]
    )

    data["users"] = simulate_users(
        data["users"]
    )

    data["carts"] = simulate_carts(
        data["carts"]
    )

    return data      
