#!/bin/bash

echo "🔧 Actualizando sistema..."
sudo apt update && sudo apt upgrade -y

echo "📦 Instalando herramientas básicas..."
sudo apt install -y git vim docker.io python3 python3-pip

echo "🐳 Configurando Docker..."
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -aG docker ubuntu

echo "✅ Entorno listo para trabajar 🚀"
