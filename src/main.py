from fastapi import FastAPI

from db.blobdb import BlobDB


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/blobdb/")
def try_blob():
    blobdb = BlobDB()
    b_ver_str = blobdb.try_azure_blob()
    return {"version": b_ver_str}
