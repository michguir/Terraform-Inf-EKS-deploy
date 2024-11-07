import boto3
from botocore.exceptions import ClientError

# Crear un cliente EC2
ec2_client = boto3.client('ec2')

# Lista de IDs de las instancias EC2 que deseas detener
instance_ids = ['i-0e451334cfbea8d1b', 'i-0e4efa04c23ec1e8e']

try:
    # Detener las instancias
    response = ec2_client.stop_instances(InstanceIds=instance_ids)
    
    # Mostrar el estado de la operación
    print(f"Se está deteniendo las instancias: {instance_ids}")
    print(response)
except ClientError as e:
    print(f"Error al detener las instancias: {e}")