from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from ingestion.ingestion import fetch_data
from ingestion.ingestion import get_total

def download_endpoint(endpoint,limit=30):
    total=get_total(endpoint)
    print(f"{endpoint} contains {total} records")
    skips=range(0,total,limit)
    records=[]
    with ThreadPoolExecutor(max_workers=6) as executor:
        future_to_pages={
            executor.submit(fetch_data,endpoint,limit,skip):
            skip for skip in skips
        }
        for future in as_completed(future_to_pages):
            skip=future_to_pages[future]
            try:
                response=future.result()
                data=response[endpoint]
                records.extend(data)
                print(
                    f"{endpoint.upper():10}"
                    f"| Page {skip:3}"
                    f"| Records {len(data):2}"
                )
            except Exception as e:
                print(f"{endpoint} page {skip} failed")
                print(e)

    return records



def download_all():
    endpoints=["users","products","carts"]
    all_data={}
    

    with ThreadPoolExecutor(max_workers=3) as executor:
        future_to_endpoints={executor.submit(download_endpoint,endpoint):endpoint
        for endpoint in endpoints
        }

        for future in as_completed(future_to_endpoints):
            endpoint=future_to_endpoints[future]
            try:
                all_data[endpoint] = future.result()

                print(f"{endpoint} completed")

            except Exception as e:

                print(f"{endpoint} failed")

                print(e)

    return all_data

