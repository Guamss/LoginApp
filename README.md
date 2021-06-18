Login app in python (kivy and mysql)

to make this file work you need mysql (i recommend xamp or wamp), mysql-connector and kivy

install Kivy :
`
sudo apt-get install -y \
python3-pip \
build-essential \
git \
python3 \
python3-dev \
`
install MySQL-connector:
```
pip install mysql-connector-python
```
and you need to create a database:
`
CREATE DATABASE gamedata
CREATE TABLE User (username text), (password, text)
INSERT INTO User (username, password) VALUES ('username', 'password')
Note : this project is WIP so it isn't complete
`
