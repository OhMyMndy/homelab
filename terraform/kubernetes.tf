# TODO create load balance VM with HAproxy


module "k3s" {
  source = "./modules/vm"

  for_each = {
    "kubernetes-1" = {
      vm_id      = 401,
      ip_address = "10.0.40.81",
      k3s_type = "server",
      k3s_args = "",
      k3s_server = "10.0.40.81",
    },
    "kubernetes-2" = {
      vm_id      = 402,
      ip_address = "10.0.40.82"
      k3s_type = "agent",
      k3s_args = "--server https://10.0.40.81:6443",
      k3s_server = "10.0.40.81",
    }
  }

  hostname = each.key
  tags     = ["terraform", "ubuntu", "k3s", "kubernetes"]

  vm_id = each.value.vm_id

  node_name             = local.node_name
  datastore_id          = local.datastore_id
  snippets_datastore_id = local.snippets_datastore_id
  ip_address            = "${each.value.ip_address}/24"
  cores                 = 3
  # cpu_type              = "host"
  memory                = 8000
  on_boot               = true
  disk_size             = 120

  image = proxmox_virtual_environment_download_file.ubuntu_24_04.id

  cloud_init = templatefile("./cloud-init-k3s-${each.value.k3s_type}.yml.tftpl", {
    ssh_public_key: trimspace(data.local_file.ssh_public_key.content),
    user = "mandy",
    hostname = each.key
    token = var.kubernetes_token,
    ip_address = each.value.ip_address
    k3s_type = each.value.k3s_type,
    k3s_args = each.value.k3s_args,
    k3s_server = each.value.k3s_server
  })

}
