#!/bin/sh
set -ex



expected_user='www-data'
expected_group='www-data'

user_name=$(id -nu $UID 2>/dev/null); echo $user_name
group_name=$(id -nu $GID 2>/dev/null); echo $group_name



if [ "$user_name" != '' ] && [ "$user_name" = "${expected_user}" ]; then
    usermod -u 99991 $UID
fi

if [ "$user_name" != '' ] && [ "$user_name" = "${expected_user}" ]; then
    usermod -g 99991 $UID
fi

usermod -u $UID www-data
groupmod -g $GID www-data
# first arg is `-f` or `--some-option`
if [ "${1#-}" != "$1" ]; then
	set -- apache2-foreground "$@"
fi

echo "$@"
