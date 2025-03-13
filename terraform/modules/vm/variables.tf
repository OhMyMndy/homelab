variable "hostname" {
  type = string
}

variable "tags" {
  type    = set(string)
  default = ["terraform"]
}

variable "vm_id" {
  type = number
}
variable "node_name" {
  type = string
}
variable "datastore_id" {
  type = string
}

variable "snippets_datastore_id" {
  type = string
}
variable "cloud_init" {
  type = string
}

variable "cpu_limit" {
  type    = number
  default = 128
}
variable "memory" {
  type    = number
  default = 2048
}
variable "on_boot" {
  type    = bool
  default = false
}
variable "disk_size" {
  type    = number
  default = 40
}
variable "image" {
  type = string
}

variable "cores" {
  type    = number
  default = 1
}

variable "ip_address" {
  type     = string
  nullable = true

  validation {
    condition     = var.ip_address == null || can(regex("^[0-9]+.[0-9]+.[0-9]+.[0-9]+/[0-9]+", var.ip_address))
    error_message = "Should be an IP address '0.0.0.0/0'"
  }
}

variable "cpu_type" {
  default = "EPYC-IBPB"
}