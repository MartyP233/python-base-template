git init

python -m venv env

CALL c:\Projects\{{cookiecutter.directory_name}}\env\Scripts\activate.bat

c:\Projects\{{cookiecutter.directory_name}}\env\Scripts\python.exe -m pip install --upgrade pip

pip install -r requirements.txt
pip install -r requirements_dev.txt

@pause