import boto3
from botocore.exceptions import ClientError

# Crear un cliente S3
s3_client = boto3.client('s3')

# Nombre del bucket
bucket_name = 'my-unique-backup-bucket'  # Asegúrate de que el nombre sea único

try:
    # Crear el bucket
    s3_client.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'us-west-2'  # Puedes cambiar la región si es necesario
        }
    )
    print(f"Bucket '{bucket_name}' creado exitosamente.")
except ClientError as e:
    print(f"Error al crear el bucket: {e}")

