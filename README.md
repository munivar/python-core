# Project Description

### GSHEET | REST API - Python, Google Sheet
- Python - 3.12.7
- Postgres Database - pgAdmin - 17.0
- Video URL - https://www.youtube.com/watch?v=zCEJurLGFRk

### Usage (Command and Steps)

1. setup initial project structure
- This command will display a list of all installed Python packages along with their versions
```bash
pip freeze
```
- Run the following command to generate a list of installed packages
```bash
pip freeze > requirements.txt
```
- To install Python libraries listed in a requirements.txt file, you can use the following command
```bash
pip install -r requirements.txt
```
- uninstall all the packages
```bash
pip uninstall -r requirements.txt
```

2. create virtual envioronment (Do this if require)
```bash
python -m venv myenv
```
3. activate the envioronment (Do this if require)
```bash
.\myenv\Scripts\activate
```

4. Watch Video and Create Service Account and Project

5. Update the Google Drive and Google Sheet Access Rights as per requirement

6. for starting api
```bash
python test_sheet.py
```