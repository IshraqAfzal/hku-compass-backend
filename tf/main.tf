terraform {
  backend "http" {              
  }
}

provider "aws" {
    region  = "${var.aws_region}"
}