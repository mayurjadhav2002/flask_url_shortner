
# Flask URL Shorter Application 

A Lightweight URL shortner Application built with Flask, SqlAlechemy, Bootstrap. This Application will allow you to short your own URL or host this app as a  URL Shorter Under your maintenance.

## Screenshots

![App Screenshot](https://raw.githubusercontent.com/mayurjadhav2002/flask_url_shortner/master/static/Screenshot%20from%202022-07-16%2023-26-20.png)



## Run Locally

### Installation

To deploy this project run,
Clone this Repo

```bash
  git clone https://github.com/mayurjadhav2002/flask_url_shortner.git
```
open Project File and Install Required Dependencies.
You'll Need python 3 and PIP installer for this Project.
If you already meet requirements, install packages via pip

```bash
source venv/bin/activate
```
```bash
  pip install -r requirements.txt
```

Now, open new terminal and type python3
```bash
python
```
after opening python, in terminal, run following code to create sqlalchemy database.
```bash
from main import *
db.create_all()
```
Now you can run the application on your local Machine.
Just type in cmd or terminal
```bash
python main.py
```
or
```bash
set FLASK_APP=main
flask run
```

## Contributing

Contributions are always welcome!

Please adhere to this project's `code of conduct`.


## Tech Stack

**Client:** Flask, Flask_sqlAlchemy, Bootstrap

**Server:** Flask(Gunicorn) *Self Hosted Locally*


## Authors

- [@mayurjadhav2002](https://github.com/mayurjadhav2002)

