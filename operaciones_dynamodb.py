import boto3
import sys
from datetime import datetime

# Inicializa DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
tabla = dynamodb.Table('TablaProyectoFinal')

def insertar():
    fecha_creacion = datetime.utcnow().isoformat()
    response = tabla.put_item(
        Item={
            'ID': '001',
            'FechaCreacion': fecha_creacion,
            'Nombre': 'Producto A',
            'Precio': 100
        }
    )
    print(f"✔ Registro insertado. FechaCreacion: {fecha_creacion}")

def modificar(fecha_creacion):
    response = tabla.update_item(
        Key={
            'ID': '001',
            'FechaCreacion': fecha_creacion
        },
        UpdateExpression="SET Precio = :p",
        ExpressionAttributeValues={':p': 150},
        ReturnValues="UPDATED_NEW"
    )
    print("✔ Registro modificado:", response)

def eliminar(fecha_creacion):
    response = tabla.delete_item(
        Key={
            'ID': '001',
            'FechaCreacion': fecha_creacion
        }
    )
    print("✔ Registro eliminado:", response)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("❌ Especifica la operación: insertar, modificar <fecha>, eliminar <fecha>")
        sys.exit(1)

    operacion = sys.argv[1]

    if operacion == 'insertar':
        insertar()
    elif operacion == 'modificar':
        if len(sys.argv) != 3:
            print("❌ Especifica la FechaCreacion: modificar <FechaCreacion>")
        else:
            modificar(sys.argv[2])
    elif operacion == 'eliminar':
        if len(sys.argv) != 3:
            print("❌ Especifica la FechaCreacion: eliminar <FechaCreacion>")
        else:
            eliminar(sys.argv[2])
    else:
        print("❌ Operación no reconocida. Usa: insertar, modificar <fecha>, eliminar <fecha>")

