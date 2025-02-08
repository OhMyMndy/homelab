resource "proxmox_virtual_environment_download_file" "talos_1_9_3" {
  content_type            = "iso"
  datastore_id            = "local"
  node_name               = "pve-1"
  url                     = "https://factory.talos.dev/image/ce4c980550dd2ab1b17bbf2b08801c7eb59418eafe8f279833297925d67c7515/v1.9.3/nocloud-amd64.raw.gz"
  decompression_algorithm = "gz"
  file_name               = "talos-1.9.3.iso"
  overwrite               = false
  overwrite_unmanaged     = true
}
