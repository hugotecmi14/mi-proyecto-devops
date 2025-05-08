#!/bin/bash

echo "👤 Crear nuevo usuario en el sistema"
read -p "Nombre de usuario: " usuario

# Crear usuario
sudo adduser $usuario

# Dar permisos de sudo y Docker
sudo usermod -aG sudo $usuario
sudo usermod -aG docker $usuario

echo "✅ Usuario '$usuario' creado con acceso a sudo y Docker"
