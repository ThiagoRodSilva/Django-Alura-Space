#!/bin/bash
set -e
echo "📦 Criando ambiente virtual..."
python3.12 -m venv venv
source venv/bin/activate

echo "🚀 Instalando dependências..."
pip install --upgrade pip
pip install -r requirements.txt

echo "🎨 Coletando arquivos estáticos..."
python3.12 manage.py collectstatic --noinput --clear

echo "✅ Build finalizado com sucesso!"