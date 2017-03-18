export MY_IP=$(ip route get 8.8.8.8 | awk '/8.8.8.8/ {print $NF}')
sed -E -i 's/(IPV4_ADDRESS=)(.*)/\1${MY_IP}/g' /etc/pihole/setupVars.conf