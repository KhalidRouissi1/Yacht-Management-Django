echo "BUILD START"
python3.10 -m pip install requirmenets.txt
python3.10 manage.py collectstatic --noinput --clear
echo "BUILD END"
