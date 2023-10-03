Postblog
===

## About
Study work for FU

```bash
$ wsl --install
```
If WSL is already installed on the system, use 
```bash
$ wsl --install -d <DistroName>
```

For more info:
* https://learn.microsoft.com/windows/wsl/install
* https://learn.microsoft.com/windows/wsl/setup/environment
* https://www.jetbrains.com/help/pycharm/using-wsl-as-a-remote-interpreter.html


### Local environment

#### Install required packages

```bash
$ sudo apt update
$ sudo apt install build-essential libssl-dev zlib1g-dev \
  libbz2-dev libreadline-dev libsqlite3-dev curl llvm \
  libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev \
  libffi-dev liblzma-dev libsasl2-dev python3-dev libldap2-dev \
  postgresql postgresql-contrib git
```
##### Install python
Ubuntu
```bash
$ sudo apt install python3.10 python3-pip 
```

```bash
$ pip install virtualenv
```

#### Clone repository

```bash
$ git clone https://github.com/Svjashennik/postblog.git && cd postblog
```

#### Install virtual environment

```bash
$ python3.10 -m venv .env
$ source .env/bin/activate
```

#### Install python requirement modules

```bash
(.env)$ pip install -r requirements.txt
```
#### Database initialization

##### Connect to database
```bash
(.env)$ sudo service postgresql start
(.env)$ sudo -u postgres psql
```

##### In psql
```postgresql
postgres=# \password postgres
postgres=# CREATE DATABASE postblog;
postgres=# \q
```
##### Migrate
```bash
(.env)$ ./intranet/manage.py migrate
```

##### Run Server
#### Run project components

```bash
(.env)$ ./intranet/manage.py runserver
```
Or
```bash
(.env)$ docker-compose up
```