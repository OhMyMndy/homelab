#!/bin/sh
set -x



expected_user='www-data'
expected_group='www-data'

user_name=$(id -nu $UID 2>/dev/null);
group_name=$(getent passwd "$GID" | cut -d: -f1);


if [ "$user_name" != '' ] && [ "$user_name" != "${expected_user}" ]; then
    usermod -u 99991 $(id ${user_name})
fi

if [ "$group_name" != '' ] && [ "$group_name" != "${expected_group}" ]; then
    groupmod -g 99991 $(getent group ${group_name} |  cut -d: -f1)
fi

usermod -u $UID www-data
groupmod -g $GID www-data
# first arg is `-f` or `--some-option`
if [ "${1#-}" != "$1" ]; then
	set -- apache2-foreground "$@"
fi

exec "$@"
