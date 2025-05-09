import boto3
import os

# Configura tu bucket y la ruta del archivo que deseas subir
BUCKET_NAME = 'bucket-proyecto-final-hugo'
LOCAL_FILE_PATH = '/home/ssm-user/mi-proyecto-devops/README.md'  # Cambia por la ruta de tu archivo
S3_OBJECT_NAME = 'README.md'  # Nombre con el que se guardará en S3

def subir_archivo_s3(bucket_name, local_file, s3_object_name):
    try:
        s3_client = boto3.client('s3')
        s3_client.upload_file(local_file, bucket_name, s3_object_name)
        print(f'✅ Archivo {local_file} subido como {s3_object_name} en el bucket {bucket_name}.')
    except Exception as e:
        print(f'❌ Error al subir el archivo: {e}')

if __name__ == '__main__':
    if os.path.exists(LOCAL_FILE_PATH):
        subir_archivo_s3(BUCKET_NAME, LOCAL_FILE_PATH, S3_OBJECT_NAME)
    else:
        print(f'❌ El archivo {LOCAL_FILE_PATH} no existe.')
