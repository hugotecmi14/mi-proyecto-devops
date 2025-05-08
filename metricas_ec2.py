import boto3
from datetime import datetime, timedelta

ec2 = boto3.client('ec2', region_name='us-east-1')
cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')

def obtener_metricas(instance_id):
    fin = datetime.utcnow()
    inicio = fin - timedelta(hours=1)

    metricas = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
        StartTime=inicio,
        EndTime=fin,
        Period=300,
        Statistics=['Average']
    )

    for punto in metricas['Datapoints']:
        print(f"Instancia {instance_id} - Promedio CPU: {punto['Average']:.2f}% - {punto['Timestamp']}")

if __name__ == "__main__":
    # Solo un ejemplo de instancia, se puede automatizar con describe_instances()
    obtener_metricas("i-0123456789abcdef0")
