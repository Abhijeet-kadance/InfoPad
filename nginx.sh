#!/bin/bash
 
echo "NGINX SETUP: INITIALIZED...."

sudo cp -rf  ideapad.conf /etc/nginx/conf.d

chmod 710 /var/lib/jenkins/workspace/django-cicd

sudo nginx -t 

sudo systemctl start nginx
sudo systemctl enable nginx

echo "Nginx has been started"

sudo systemctl status nginx

