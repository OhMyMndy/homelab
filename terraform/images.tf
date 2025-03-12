resource "proxmox_virtual_environment_download_file" "ubuntu_24_04" {
  content_type        = "iso"
  datastore_id        = "shared-nfs"
  node_name           = "pve-2"
  url                 = "https://cloud-images.ubuntu.com/noble/current/noble-server-cloudimg-amd64.img"
  overwrite           = false
  overwrite_unmanaged = true
}

resource "proxmox_virtual_environment_download_file" "ubuntu_24_04_desktop" {
  content_type        = "iso"
  datastore_id        = "local"
  node_name           = "pve-2"
  url                 = "https://releases.ubuntu.com/noble/ubuntu-24.04.2-desktop-amd64.iso"
  overwrite           = true
  overwrite_unmanaged = true
}