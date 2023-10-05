#!/usr/bin/env bash
#Prepare your web servers 

#install nginx if not already installed

echo -e "Script start..."

function install() {
    #check if application is alreay installed
    # command -v "$1" &> /dev/null

    # if [ $? -ne 0 ]
    if ! command -v "$1"
    then
        echo -e "Installing: $1\n\n"

        echo -e "Updating system\n"
        sudo apt-get update -y -qq

        echo -e "Installation...\n"
        sudo apt-get install -y "$1" -qq
        echo -e "\n\n"
    else
        echo "$1 is already installed."
        echo -e "\n"
    fi
}


install nginx;

echo -e "Creating required folders.\n"
folders=( data data/web_static data/web_static/releases data/web_static/shared data/web_static/releases/test )

for i in "${folders[@]}"
do
    echo -e "Creating folder: $i.\n"
    mkdir -p  "$i"
done

#Creation of fake HTML file for testing
path="data/web_static/releases/test/index.html"
content="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

echo -e "Creation of fake HTML file for testing...\n"
echo "$content" | sudo tee "$path"


#Create a symbolic link
echo -e "Create a symbolic link.\n"
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current


# set files permissions and owner
chown -hR ubuntu:ubuntu /data/

#confing nginx
echo -e "Start nginx configuration.\n"

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
	alias /data/web_static/current;
	index index.html index.htm;
    }

    location /redirect_me {
	return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default




echo -e "Start Nginx...\n"
# service nginx restart
if [ "$(pgrep -c nginx)" -le 0 ]
then
	sudo service nginx start
else
	sudo service nginx restart
fi