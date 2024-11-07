import boto3

# Crear un cliente S3
s3_client = boto3.client('s3')

def delete_s3_bucket(bucket_name):
    # Eliminar el bucket S3
    s3_client.delete_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' eliminado.")

bucket_name = 'my-unique-bucket-name-12345'  # Reemplaza con el nombre de tu bucket
delete_s3_bucket(bucket_name)