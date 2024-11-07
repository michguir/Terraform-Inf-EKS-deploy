import boto3

# Crear un cliente IAM
iam_client = boto3.client('iam')

def list_iam_roles():
    # Listar roles IAM
    response = iam_client.list_roles()
    for role in response['Roles']:
        print(f"Rol: {role['RoleName']}")

list_iam_roles()