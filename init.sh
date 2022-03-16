sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
cd /home/box/web/ask
sudo gunicorn --bind=0.0.0.0:8000 ask.wsgi
cd ../
