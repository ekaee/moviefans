# Moviefans

Moviefans is a web app made with django that provides users a platform to discuss and rate movies.

*Internet Technology Team Project - TEAM SEGW*

## Setup

- Clone repository

```bash
git clone https://github.com/ekaee/moviefans.git
```

- Install [python3; setup python-venv](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04) to create a virtual environment before installing the dependencies of the project.

```bash
cd moviefans
python3 -m venv env

# In case you are using anaconda;
conda create -n env python=3.7.5
```

```bash
# Activating the environment
source env/bin/activate

# In case you are using anaconda;
conda activate env
```

- Install all the required dependecies using the package manager [pip](https://pip.pypa.io/en/stable/).

```bash
pip install -r requirements.txt
```

## Usage

- In the project folder, go into 'moviefansapp' then make migrations and migrate

```bash
cd moviefansapp
python manage.py makemigrations
python manage.py makemigrations main
```
```bash
python manage.py migrate
```

- Populate sample data in database by running population_scripy.py

```bash
python population_script.py
```

- Run the server

```bash
python manage.py runserver
```

- Credentials to access different parts of the website

```
# User ->
http://127.0.0.1:8000/ or http://localhost:8000/

# Sample User Credentails
Username: testuser
password: testabc123

New user can be made by registration in the webapp
```

## License
[GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)
