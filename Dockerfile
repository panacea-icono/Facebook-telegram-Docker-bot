# Facebook Messenger Bot - Dockerfile
# Desarrollado por Panacea Icono S.A.

FROM python:3.11-slim

# Metadatos
LABEL maintainer="Panacea Icono S.A. <info@panacea-icono.com>"
LABEL description="Bot de Facebook Messenger para gestión de redes sociales"
LABEL version="1.0.0"

# Variables de entorno
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PORT=8080

# Crear usuario no-root para seguridad
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Establecer directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiar archivos de dependencias
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar código de la aplicación
COPY app.py .

# Cambiar propietario de los archivos
RUN chown -R appuser:appuser /app

# Cambiar a usuario no-root
USER appuser

# Exponer puerto
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8080/health')" || exit 1

# Comando de inicio
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "4", "--timeout", "120", "--keep-alive", "2", "--max-requests", "1000", "--max-requests-jitter", "100", "app:app"]
