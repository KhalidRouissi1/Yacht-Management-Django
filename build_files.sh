echo "BUILD START"
python3.9 --version  # Check the Python version
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear
echo "BUILD END"
