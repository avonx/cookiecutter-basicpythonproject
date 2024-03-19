if [ -d "venv" ]; then
    echo "Virtual environment already exists"
    source venv/bin/activate
    exit 1
fi
python3 -m venv venv
source venv/bin/activate