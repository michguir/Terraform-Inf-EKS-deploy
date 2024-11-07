import boto3

# Crear una sesión de EC2
ec2_client = boto3.client('ec2')

def stop_instance(instance_id):
    # Detener la instancia EC2
    ec2_client.stop_instances(InstanceIds=[instance_id])
    print(f'Instancia {instance_id} detenida.')

def start_instance(instance_id):
    # Iniciar la instancia EC2
    ec2_client.start_instances(InstanceIds=[instance_id])
    print(f'Instancia {instance_id} iniciada.')

instance_id = 'i-xxxxxxxxxxxxxxx'  # Reemplaza con tu ID de instancia
stop_instance(instance_id)
start_instance(instance_id)