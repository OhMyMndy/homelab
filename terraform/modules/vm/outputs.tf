
output "ip_address" {
  value = zipmap(proxmox_virtual_environment_vm.this.network_interface_names, proxmox_virtual_environment_vm.this.ipv4_addresses)["eth0"]
}
