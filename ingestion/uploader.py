import json
from datetime import datetime
from azure.storage.blob import BlobServiceClient
from config import CONNECTION_STRING,BRONZE_CONTAINER

def generate_formet(dataset,batch_id):
    

    now=datetime.utcnow()

    year=now.strftime("%Y")
    month=now.strftime("%m")
    day=now.strftime("%d")

    timestamp=now.strftime("%Y%m%d_%H%M%S")

    return f"raw/{dataset}/{year}/{month}/{day}/{dataset}_batch{batch_id}_{timestamp}.json"


def upload_dataset(dataset,records,batch_id):
    blob_name=generate_formet(dataset,batch_id)
    blob_service_client=BlobServiceClient.from_connection_string(CONNECTION_STRING)
    blob_client=blob_service_client.get_blob_client(
        container=BRONZE_CONTAINER,
        blob=blob_name
    )

    json_data="\n".join(
        json.dumps(record)
        for record in records
    )

    blob_client.upload_blob(
        json_data,
        overwrite=True
    )
    print(f"{dataset.upper()} Uploaded")
    print(blob_name)

def upload_all(data,batch_id):

    for dataset,records in data.items():

        upload_dataset(
            dataset,
            records,
            batch_id
        )



    


