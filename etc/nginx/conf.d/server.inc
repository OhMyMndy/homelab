proxy_set_header X-Forwarded-For $remote_addr;
#auth_basic $mysite_hascookie;
#auth_basic_user_file /etc/nginx/conf.d/.htpasswd;
# https://blog.liip.ch/archive/2017/01/12/no-nginx-basic-auth-with-either-network-or-cookie-set.html
add_header Set-Cookie "letmein=someRandomValue;max-age=3153600000;path=/"; #set that special cookie, when everything is ok
