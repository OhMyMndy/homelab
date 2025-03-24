# module "omada-sc" {
#   source = "./modules/vm"
#
#   hostname = "omada-sc"
#   tags     = ["terraform", "ubuntu", "omada-sc"]
#
#   vm_id = 302
#
#   node_name             = local.node_name
#   datastore_id          = local.datastore_id
#   snippets_datastore_id = local.snippets_datastore_id
#   ip_address            = "10.0.40.29/24"
#   cores                 = 1
#   cpu_type              = "host"
#   memory                = 1024
#   on_boot               = true
#   disk_size             = 20
#
#   image = proxmox_virtual_environment_download_file.ubuntu_24_04.id
#
#   cloud_init = templatefile("./cloud-init-omada-sc.yml.tftpl", {
#     ssh_public_key: trimspace(data.local_file.ssh_public_key.content),
#     user = "mandy",
#     hostname = "omada-sc"
#   })
#
# }
