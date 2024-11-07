import boto3
from botocore.exceptions import ClientError

# Crear un cliente de EC2 y EKS
ec2_client = boto3.client('ec2')
eks_client = boto3.client('eks')

# Nombre del clúster EKS
cluster_name = 'demo-cluster'

# Obtener los grupos de nodos del clúster
response = eks_client.list_nodegroups(clusterName=cluster_name)

# Obtener los IDs de los nodos
nodegroup_ids = response['nodegroups']

# Iniciar las instancias de los nodos
for nodegroup_id in nodegroup_ids:
    # Obtener las instancias del grupo de nodos
    nodegroup_details = eks_client.describe_nodegroup(clusterName=cluster_name, nodegroupName=nodegroup_id)
    instance_ids = [instance['instanceId'] for instance in nodegroup_details['nodegroup']['instances']]
    
    # Iniciar las instancias EC2
    try:
        ec2_client.start_instances(InstanceIds=instance_ids)
        print(f"Iniciando instancias: {instance_ids}")
    except ClientError as e:
        print(f"Error al iniciar las instancias: {e}")
