import boto3

autoscaling = boto3.client('autoscaling')

def listar_grupos():
    response = autoscaling.describe_auto_scaling_groups()
    for grupo in response['AutoScalingGroups']:
        print(f"Grupo: {grupo['AutoScalingGroupName']}")
        print(f"  Mínimo: {grupo['MinSize']} - Máximo: {grupo['MaxSize']}")
        print(f"  Instancias: {len(grupo['Instances'])}")

if __name__ == "__main__":
    listar_grupos()
