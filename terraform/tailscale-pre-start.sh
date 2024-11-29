#!/usr/bin/env bash

vm_id="$1"

phase="$2"

if [[ "$phase" == "pre-start" ]]; then
  if ! grep -q "lxc.cgroup2.devices.allow: c 10:200 rwm" "/etc/pve/lxc/$vm_id.conf"; then
    echo "lxc.cgroup2.devices.allow: c 10:200 rwm" >>"/etc/pve/lxc/$vm_id.conf"
  fi
  if ! grep -q "lxc.mount.entry: /dev/net dev/net none bind,create=dir" "/etc/pve/lxc/$vm_id.conf"; then
    echo "lxc.mount.entry: /dev/net dev/net none bind,create=dir" >>"/etc/pve/lxc/$vm_id.conf"
  fi
fi
