#python code for automating the download
import requests
import os
# importing the two libraries , os for performing file operations on our operating system and requests for dowloading the file using the url. 
def download_file(url, dest_folder):
    # Checking  if the destination folder exists, create it if it doesn't
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    # Send a GET request to the URL to download the file, stream the response
    response = requests.get(url, stream=True)
    
    # Extract the file name from the URL
    file_name = os.path.join(dest_folder, url.split("/")[-1])
    #here the split function is used to extract the specific file name
    
    # Open a file in binary write mode to save the downloaded content
    with open(file_name, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            # Write each chunk to the file
            file.write(chunk)
    
    # Print a message indicating successful download
    print(f"Downloaded {file_name}")

# Example usage:
#usually we have a s3 bucket or azure blob storage where we get these files and using spark functionalities we read the delta/parquet/csv files from that storage account
# databricks platform or something else
url = "https://example.com/nyc_taxi_data_2019.csv"
download_file(url, "./data")