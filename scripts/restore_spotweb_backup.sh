cd ~/Docker/homelab

docker exec -it  mysql bash -c "mysql -u root -p\$MYSQL_ROOT_PASSWORD -e 'drop database if exists spotweb; create database spotweb'"

docker exec -i  mysql bash -c "mysql -u root -p\$MYSQL_ROOT_PASSWORD spotweb" < /tank/backups/spotweb/spotweb_backup_20180106-210127.sql
