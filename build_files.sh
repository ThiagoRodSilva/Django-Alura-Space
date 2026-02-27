# build_files.sh
echo "BUILD START"

# Instala as dependências
python3.14 -m pip install -r requirements.txt

# Faz as migrações e coleta os arquivos estáticos
python3.14 manage.py makemigrations --noinput
python3.14 manage.py migrate --noinput
python3.14 manage.py collectstatic --noinput --clear

echo "BUILD END"