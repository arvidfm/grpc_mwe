for i in {1..100}; do
  echo "Attempt $i..."
  poetry run python mwe.py client
done
