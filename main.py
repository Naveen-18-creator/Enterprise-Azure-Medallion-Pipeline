from ingestion.multithreading import download_all
from ingestion.simulator import simulate_all

data=download_all()
data=simulate_all(data)
products=data["products"]
users=data["users"]
carts=data["carts"]

print("="*40)
print(f"Products : {len(products)}")
print(f"Users    : {len(users)}")
print(f"Carts    : {len(carts)}")
print("=" * 40)




