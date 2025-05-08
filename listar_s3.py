import boto3

s3 = boto3.client('s3')

def listar_buckets():
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        nombre = bucket['Name']
        print(f"📦 Bucket: {nombre}")
        listar_objetos(nombre)

def listar_objetos(bucket_name):
    response = s3.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in response:
        for obj in response['Contents']:
            print(f"  └── {obj['Key']} ({obj['Size']} bytes)")
    else:
        print("  └── (Sin objetos)")

if __name__ == "__main__":
    listar_buckets()
