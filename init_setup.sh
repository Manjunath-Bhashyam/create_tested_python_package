echo [$(date)]: "START"
echo [$(date)]: "Creating virtual environment"
python -m venv env
echo [$(date)]: "Activating virtual environment"
source env/scripts/activate
echo [$(date)]: "installing dev requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "END"