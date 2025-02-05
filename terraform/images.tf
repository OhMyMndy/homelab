resource "proxmox_virtual_environment_download_file" "latest_static_ubuntu_24_noble_qcow2_img" {
  content_type        = "iso"
  datastore_id        = "local"
  node_name           = "pve-1"
  url                 = "https://cloud-images.ubuntu.com/noble/current/noble-server-cloudimg-amd64.img"
  overwrite           = false
  overwrite_unmanaged = true
}

resource "proxmox_virtual_environment_download_file" "ubuntu_24_04_desktop" {
  content_type        = "iso"
  datastore_id        = "local"
  node_name           = "pve-1"
  url                 = "https://releases.ubuntu.com/24.04.1/ubuntu-24.04.1-desktop-amd64.iso"
  overwrite           = false
  overwrite_unmanaged = true
}
resource "proxmox_virtual_environment_download_file" "alma-linux-9-5" {
  content_type        = "iso"
  datastore_id        = "local"
  node_name           = "pve-1"
  url                 = "https://repo.almalinux.org/almalinux/9.5/isos/x86_64/AlmaLinux-9.5-x86_64-dvd.iso"
  checksum            = "3947accd140a2a1833b1ef2c811f8c0d48cd27624cad343992f86cfabd2474c9"
  checksum_algorithm  = "sha256"
  overwrite           = false
  overwrite_unmanaged = true
}

resource "proxmox_virtual_environment_download_file" "fedora-41-kde-mobile" {
  content_type        = "iso"
  datastore_id        = "local"
  node_name           = "pve-1"
  url                 = "https://download.fedoraproject.org/pub/fedora/linux/releases/41/Spins/x86_64/iso/Fedora-KDE-Mobile-Live-41-1.4.x86_64.iso"
  checksum            = "0013147b27a5082d07f0c3e5851c1182b7f10980bb690a9e710d735e96cb81cb"
  checksum_algorithm  = "sha256"
  overwrite           = false
  overwrite_unmanaged = true
}



resource "proxmox_virtual_environment_download_file" "fedora_41" {
  content_type        = "iso"
  datastore_id        = "local"
  node_name           = "pve-1"
  url                 = "https://download.fedoraproject.org/pub/fedora/linux/releases/41/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-41-1.4.iso"
  checksum            = "a2dd3caf3224b8f3a640d9e31b1016d2a4e98a6d7cb435a1e2030235976d6da2"
  checksum_algorithm  = "sha256"
  overwrite           = false
  overwrite_unmanaged = true
}
resource "proxmox_virtual_environment_download_file" "opensense_24_7" {
  content_type            = "iso"
  datastore_id            = "local"
  node_name               = "pve-1"
  url                     = "https://mirror.ams1.nl.leaseweb.net/opnsense/releases/24.7/OPNsense-24.7-dvd-amd64.iso.bz2"
  checksum                = "4452df716417cac324bb06322fc4428870ac2a64fd6ae47675a421e8db0a18b5"
  checksum_algorithm      = "sha256"
  overwrite               = false
  overwrite_unmanaged     = true
  decompression_algorithm = "bz2"
  file_name               = "OPNsense-24.7-dvd-amd64.iso"
}

# customization:
#     systemExtensions:
#         officialExtensions:
#             - siderolabs/qemu-guest-agent
## Schematic ID: ce4c980550dd2ab1b17bbf2b08801c7eb59418eafe8f279833297925d67c7515
resource "proxmox_virtual_environment_download_file" "talos_1_9_3" {
  content_type            = "iso"
  datastore_id            = "local"
  node_name               = "pve-1"
  url                     = "https://factory.talos.dev/image/ce4c980550dd2ab1b17bbf2b08801c7eb59418eafe8f279833297925d67c7515/v1.9.3/nocloud-amd64.raw.gz"
  decompression_algorithm = "gz"
  file_name               = "talos-1.9.3.iso"
  overwrite               = true
  overwrite_unmanaged     = true
}


resource "proxmox_virtual_environment_download_file" "ubuntu_noble_lxc" {
  content_type = "vztmpl"
  datastore_id = "local"
  node_name    = "pve-1"
  url          = "http://download.proxmox.com/images/system/ubuntu-24.04-standard_24.04-2_amd64.tar.zst"
}
