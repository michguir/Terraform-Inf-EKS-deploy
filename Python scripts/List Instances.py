import boto3

# Crear una sesión de EC2
ec2_client = boto3.client('ec2')

def list_instances():
    # Listar todas las instancias EC2
    response = ec2_client.describe_instances()
    
    # Iterar sobre las instancias y mostrar detalles clave
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print(f"ID de Instancia: {instance['InstanceId']}")
            print(f"Estado: {instance['State']['Name']}")
            if 'PublicIpAddress' in instance:
                print(f"IP Pública: {instance['PublicIpAddress']}")
            print("-" * 20)

list_instances()