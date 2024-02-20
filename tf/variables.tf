variable ecr_repo_api {
  type = string
}

variable ecr_repo_proxy {
  type = string
}

variable cluster_name {
  type = string
  default = "cluster-1"
}

variable image_tag {
  type = string
}

variable aws_region {
  type = string
}

variable cloudwatch_group {
  type = string
  default = "ecs-cloudwatch-group"
}