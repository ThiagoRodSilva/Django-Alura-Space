#!/bin/bash
set -e  # para o script se algo falhar

echo "📦 Instalando dependências..."
pip install -r requirements.txt

echo "🔄 Rodando migrações..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "🎨 Coletando estáticos..."
python manage.py collectstatic --noinput

echo "✅ Build concluído!"