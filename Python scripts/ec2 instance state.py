import boto3

# Crear un cliente EC2
ec2_client = boto3.client('ec2')

def get_instance_state(instance_id):
    # Obtener el estado de la instancia EC2
    response = ec2_client.describe_instances(InstanceIds=[instance_id])
    state = response['Reservations'][0]['Instances'][0]['State']['Name']
    print(f"El estado de la instancia {instance_id} es: {state}")

instance_id = 'i-xxxxxxxxxxxxxxxxx'  # Reemplaza con el ID de tu instancia
get_instance_state(instance_id)