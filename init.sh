sudo ln -sf /home/box/web/etc/nginx.cong /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo gunicorn -c hello.py hello:wsgi_app
