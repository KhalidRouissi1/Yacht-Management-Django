echo "BUILD START"
python3 --version  # Add this line to check the Python version
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput --clear
echo "BUILD END"
