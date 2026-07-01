from ingestion.multithreading import download_all
from ingestion.simulator import simulate_all
from ingestion.uploader import upload_all
import time
def main():

    for batch in range(1,6):
        print("="*60)
        print(f"Starting Batch {batch}")
        print("="*60)

        data=download_all()
        data=simulate_all(data)
        upload_all(data,batch)
        print(f"Batch {batch} Completed")

        if batch<5:

            print(f"Waiting 30 Seconds...\n")

            time.sleep(5)

        

        print("="*40)
        print(f"Products : {len(data["products"])}")
        print(f"Users    : {len(data["users"])}")
        print(f"Carts    : {len(data["carts"])}")
        print("=" * 40)

        



if __name__ == "__main__":
    main()

