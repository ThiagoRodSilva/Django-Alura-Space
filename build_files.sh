echo "Instalando dependências..."
python3 -m pip install -r requirements.txt

echo "Fazendo migrações..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "Coletando arquivos estáticos..."
python3 manage.py collectstatic --noinput