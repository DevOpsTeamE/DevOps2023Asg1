mkdir devops
mv DevOps2023Asg1/controllers devops
mv DevOps2023Asg1/static devops
mv DevOps2023Asg1/templates devops
mv DevOps2023Asg1/database_setup.sql devops
mv DevOps2023Asg1/predatabase_setup.sql devops
mv DevOps2023Asg1/main.py devops
mv DevOps2023Asg1/nginx.config devops
sudo rm -rf DevOps2023Asg1

cd devops

sudo pkill bash
sudo apt update
sudo apt --assume-yes install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools
sudo apt --assume-yes install python3-venv
sudo apt update
sudo apt --assume-yes install mysql-server
sudo systemctl start mysql.service
sudo systemctl status mysql.service

sudo mysql --user=root --password=root < predatabase_setup.sql
sudo mysql --user=root --password=root < database_setup.sql

sudo apt --assume-yes install nginx
sudo mv -f nginx.config /etc/nginx/sites-available/devops
sudo ln -sf /etc/nginx/sites-available/devops /etc/nginx/sites-enabled
sudo systemctl restart nginx

python3 -m venv DevOpsEnv
source DevOpsEnv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install Flask
python3 -m pip install mysql-connector-python
python3 -m pip install wheel
python3 -m pip install gunicorn flask
sudo ufw allow 5000
sudo apt update
gunicorn -w 4 'main:create_app()'