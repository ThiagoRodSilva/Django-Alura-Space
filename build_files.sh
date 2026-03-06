#!/bin/bash
set -e  # Para o script se qualquer comando falhar

echo "📦 Atualizando pip..."
python3 -m ensurepip --upgrade || true
python3 -m pip install --upgrade pip

echo "📦 Instalando dependências do requirements.txt..."
python3 -m pip install -r requirements.txt

echo "🔄 Rodando migrações..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "🎨 Coletando arquivos estáticos..."
python3 manage.py collectstatic --noinput

echo "✅ Build concluído com sucesso!"