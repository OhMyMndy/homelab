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

# # Schematic ID: 501dea708aa95f4a8c32444df660bc209e67fc82fb1e831a830fe380d9a89af5https://releases.ubuntu.com/24.04.1/ubuntu-24.04.1-desktop-amd64.iso
# # https://factory.talos.dev/?arch=amd64&cmdline-set=true&extensions=-&extensions=siderolabs%2Fbtrfs&extensions=siderolabs%2Ffuse3&extensions=siderolabs%2Fiscsi-tools&extensions=siderolabs%2Fkata-containers&extensions=siderolabs%2Fmdadm&extensions=siderolabs%2Fqemu-guest-agent&extensions=siderolabs%2Ftailscale&extensions=siderolabs%2Futil-linux-tools&extensions=siderolabs%2Fzfs&platform=nocloud&target=cloud&version=1.8.3
# customization:
#    systemExtensions:
#        officialExtensions:
#            - siderolabs/btrfs
#            - siderolabs/fuse3
#            - siderolabs/iscsi-tools
#            - siderolabs/kata-containers
#            - siderolabs/mdadm
#            - siderolabs/qemu-guest-agent
#            - siderolabs/tailscale
#            - siderolabs/util-linux-tools
#            - siderolabs/zfs
resource "proxmox_virtual_environment_download_file" "talos_1_8_3" {
  content_type        = "iso"
  datastore_id        = "local"
  node_name           = "pve-1"
  url                 = "https://factory.talos.dev/image/501dea708aa95f4a8c32444df660bc209e67fc82fb1e831a830fe380d9a89af5/v1.8.3/nocloud-amd64.iso"
  file_name           = "talos-1.8.3.iso"
  overwrite           = false
  overwrite_unmanaged = true
}


resource "proxmox_virtual_environment_download_file" "ubuntu_noble_lxc" {
  content_type = "vztmpl"
  datastore_id = "local"
  node_name    = "pve-1"
  url          = "http://download.proxmox.com/images/system/ubuntu-24.04-standard_24.04-2_amd64.tar.zst"
}
