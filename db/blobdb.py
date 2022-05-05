# import os
from datetime import datetime, timedelta
from azure.storage.blob import (
    BlobServiceClient, BlobSasPermissions, BlobClient, ContainerClient, __version__, generate_blob_sas
)


class BlobDB:

    def try_azure_blob(self):
        # connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
        # Blob service にのみ接続する場合、接続文字列は次のようになります。
        # DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;
        connect_str = "DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;"
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        container_name = "container0504"
        blob_name = "tabe-2023images.jpg"
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        # if blob_client.exists():
        #     return "Exist."
        # return "False."


        token = generate_blob_sas(
            blob_client.account_name,
            blob_client.container_name,
            blob_client.blob_name,
            snapshot=blob_client.snapshot,
            account_key=blob_client.credential.account_key,
            permission=BlobSasPermissions(read=True),
            expiry=datetime.utcnow() + timedelta(hours=1),
        )

        sas_blob = BlobClient.from_blob_url(blob_client.url, credential=token)
        return sas_blob.url
