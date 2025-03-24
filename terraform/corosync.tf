module "corosync-1" {
  source = "./modules/vm"
  count = 0

  hostname = "corosync-1"
  tags     = ["terraform", "ubuntu", "corosync"]

  vm_id = 301

  node_name             = local.node_name
  datastore_id          = local.datastore_id
  snippets_datastore_id = local.snippets_datastore_id
  ip_address            = "10.0.40.9/24"
  cores                 = 1
  cpu_type              = "host"
  memory                = 256
  on_boot               = true
  disk_size             = 20

  image = proxmox_virtual_environment_download_file.ubuntu_24_04.id

  cloud_init = templatefile("./cloud-init-corosync.yml.tftpl", {
    ssh_public_key: trimspace(data.local_file.ssh_public_key.content),
    user = "mandy",
    hostname = "corosync-1"
  })

}
