# run $ source venv.sh to create a virtual environment
if [ -d "venv" ]; then
    echo "Virtual environment already exists"
    source venv/bin/activate
fi
python3 -m venv venv
source venv/bin/activate