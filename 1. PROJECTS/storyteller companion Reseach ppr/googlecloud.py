googlecloud.py
import os
from google.cloud import storage

def upload_blob(bucket_name, source_file_path, destination_blob_name):
    """Uploads a file to the Google Cloud Storage bucket."""
    # Initialize the client with the service account key
    storage_client = storage.Client.from_service_account_json("complete-flash-411506-1e6791534c29.json")

    # Get the bucket
    bucket = storage_client.bucket(bucket_name)

    # Upload the file
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_path)

    print(f"File {source_file_path} uploaded to {bucket_name} as {destination_blob_name}.")

# Set your Google Cloud Storage bucket name
bucket_name = "your_bucket_name"

# Set the source file path
source_file_path = "newtoto.wav"  # Replace with the path to your file

# Check if the file exists
if os.path.isfile(source_file_path):
    # Extract the file name from the path
    file_name = os.path.basename(source_file_path)
    
    # Check if the file has the correct extension
    if file_name.endswith(".wav"):
        # Define the destination blob name
        destination_blob_name = f"uploaded/{file_name}"  # Destination blob name with a folder named "uploaded"
        
        # Upload the file
        upload_blob(bucket_name, source_file_path, destination_blob_name)
    else:
        print("File extension is not .wav.")
else:
    print("File does not exist.")