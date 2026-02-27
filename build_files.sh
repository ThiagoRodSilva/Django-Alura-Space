# build_files.sh
echo "BUILD START"

# Instala as dependências
python3.9 -m pip install -r requirements.txt

# Faz as migrações e coleta os arquivos estáticos
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput
python3.9 manage.py collectstatic --noinput --clear

echo "BUILD END"