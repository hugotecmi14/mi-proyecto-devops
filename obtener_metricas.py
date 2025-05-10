import boto3
from datetime import datetime, timedelta

# Parámetros de recursos
INSTANCE_ID = 'i-0b8f7fbd85bc35b71'
BUCKET_NAME = 'bucket-proyecto-final-hugo'
REGION = 'us-east-1'  # Verifica que sea tu región

# Crear clientes
cloudwatch = boto3.client('cloudwatch', region_name=REGION)

def obtener_cpu_ec2(instance_id):
    """Obtiene el porcentaje de uso de CPU de una instancia EC2."""
    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
        StartTime=datetime.utcnow() - timedelta(hours=1),
        EndTime=datetime.utcnow(),
        Period=300,
        Statistics=['Average']
    )
    datapoints = response.get('Datapoints', [])
    if datapoints:
        average = sorted(datapoints, key=lambda x: x['Timestamp'])[-1]['Average']
        print(f"CPU Utilization (Instancia {instance_id}): {average:.2f}%")
    else:
        print(f"No hay datos de CPU disponibles para la instancia {instance_id}.")

def obtener_almacenamiento_s3(bucket_name):
    """Obtiene el tamaño de almacenamiento y número de objetos de un bucket S3."""
    # Tamaño de almacenamiento
    size_response = cloudwatch.get_metric_statistics(
        Namespace='AWS/S3',
        MetricName='BucketSizeBytes',
        Dimensions=[
            {'Name': 'BucketName', 'Value': bucket_name},
            {'Name': 'StorageType', 'Value': 'StandardStorage'}
        ],
        StartTime=datetime.utcnow() - timedelta(days=1),
        EndTime=datetime.utcnow(),
        Period=86400,
        Statistics=['Average']
    )
    # Conteo de objetos
    count_response = cloudwatch.get_metric_statistics(
        Namespace='AWS/S3',
        MetricName='NumberOfObjects',
        Dimensions=[
            {'Name': 'BucketName', 'Value': bucket_name},
            {'Name': 'StorageType', 'Value': 'AllStorageTypes'}
        ],
        StartTime=datetime.utcnow() - timedelta(days=1),
        EndTime=datetime.utcnow(),
        Period=86400,
        Statistics=['Average']
    )

    size_data = size_response.get('Datapoints', [])
    count_data = count_response.get('Datapoints', [])

    if size_data:
        size_bytes = sorted(size_data, key=lambda x: x['Timestamp'])[-1]['Average']
        size_mb = size_bytes / (1024 * 1024)
        print(f"Tamaño del Bucket '{bucket_name}': {size_mb:.2f} MB")
    else:
        print(f"No hay datos de almacenamiento para el bucket {bucket_name}.")

    if count_data:
        num_objects = sorted(count_data, key=lambda x: x['Timestamp'])[-1]['Average']
        print(f"Número de objetos en el Bucket '{bucket_name}': {int(num_objects)}")
    else:
        print(f"No hay datos de objetos para el bucket {bucket_name}.")

if __name__ == "__main__":
    print("\nObteniendo Métricas de EC2 y S3...\n")
    obtener_cpu_ec2(INSTANCE_ID)
    print()
    obtener_almacenamiento_s3(BUCKET_NAME)

