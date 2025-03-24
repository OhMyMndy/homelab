module "cks" {
  count = 0
  source = "./modules/vm"

  hostname = "cks"
  tags     = ["terraform", "ubuntu", "cks", "kubernetes"]

  vm_id = 200

  node_name             = local.node_name
  datastore_id          = local.datastore_id
  snippets_datastore_id = local.snippets_datastore_id
  ip_address            = "10.0.40.77/24"
  cores                 = 3
  cpu_type              = "host"
  memory                = 17000
  on_boot               = true
  disk_size             = 60

  image = proxmox_virtual_environment_download_file.ubuntu_24_04.id

  cloud_init = templatefile("./cloud-init-cks.yml.tftpl", {
    ssh_public_key: trimspace(data.local_file.ssh_public_key.content),
    user = "mandy",
    hostname = "cks"
  })

}
