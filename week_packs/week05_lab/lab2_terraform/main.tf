# Week 5 Lab 2: Terraform state, locking and drift. Nothing here touches a cloud.
terraform {
  required_version = ">= 1.10"
  required_providers {
    local = { source = "hashicorp/local", version = "~> 2.5" }
  }
}

variable "replicas" {
  type    = number
  default = 3
}

variable "slow_seconds" {
  type    = number
  default = 60
}

# The "real infrastructure": a config file Terraform owns.
resource "local_file" "app_config" {
  filename = "${path.module}/out/app.conf"
  content  = "replicas=${var.replicas}\n"
}

# A slow step so an apply holds the state lock long enough to collide with it.
resource "terraform_data" "slow_rollout" {
  triggers_replace = [local_file.app_config.content]
  provisioner "local-exec" {
    command = "echo rollout start; sleep ${var.slow_seconds}; echo rollout done"
  }
}

output "config_path" {
  value = local_file.app_config.filename
}
