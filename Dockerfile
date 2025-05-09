# Etapa 1: Copiar archivos de la app
FROM nginx:alpine AS final
COPY src/ /usr/share/nginx/html
