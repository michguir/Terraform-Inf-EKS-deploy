import boto3

# Crear un cliente EC2
ec2_client = boto3.client('ec2')

# Obtener la lista de instancias EC2
response = ec2_client.describe_instances()

# Extraer los IDs de las instancias de la respuesta
instance_ids = []
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_ids.append(instance['InstanceId'])

# Mostrar los IDs de las instancias
print("IDs de las instancias EC2:")
for instance_id in instance_ids:
    print(instance_id)