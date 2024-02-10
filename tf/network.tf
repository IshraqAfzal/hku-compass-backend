# Providing a reference to our default VPC
resource "aws_default_vpc" "default_vpc" {
}

# Providing a reference to our default subnets
resource "aws_default_subnet" "default_subnet_b" {
  availability_zone = "${var.aws_region}b"
}

resource "aws_default_subnet" "default_subnet_c" {
  availability_zone = "${var.aws_region}c"
}

resource "aws_alb" "application_load_balancer" {
  name               = "dev-api-lb-tf" # Naming our load balancer
  load_balancer_type = "application"
  subnets = [ # Referencing the default subnets
    "${aws_default_subnet.default_subnet_b.id}",
    "${aws_default_subnet.default_subnet_c.id}"
  ]
  # Referencing the security group
  security_groups = ["${aws_security_group.load_balancer_security_group.id}"]
}

# Creating a security group for the load balancer:
resource "aws_security_group" "load_balancer_security_group" {
  vpc_id      = aws_default_vpc.default_vpc.id

  ingress {
    from_port   = 0 # Allowing traffic in from port 80
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"] # Allowing traffic in from all sources
  }

  egress {
    from_port   = 0 # Allowing any incoming port
    to_port     = 0 # Allowing any outgoing port
    protocol    = "-1" # Allowing any outgoing protocol 
    cidr_blocks = ["0.0.0.0/0"] # Allowing traffic out to all IP addresses
  }
}

resource "aws_lb_target_group" "target_group" {
  name        = "target-group-web-api"
  port        = 80 # 443
  protocol    = "HTTP" # HTTPS
  target_type = "ip"
  vpc_id      = "${aws_default_vpc.default_vpc.id}" # Referencing the default VPC

  health_check {
    path = "/admin/login/"
  }
}

resource "aws_lb_listener" "listener" {
  load_balancer_arn = "${aws_alb.application_load_balancer.arn}" # Referencing our load balancer

  port              = 80 # 443
  protocol          = "HTTP" # HTTPS
  # ssl_policy        = "ELBSecurityPolicy-2016-08"
  # certificate_arn   = "${var.certificate_arn}"

  default_action {
    type             = "forward"
    target_group_arn = "${aws_lb_target_group.target_group.arn}" # Referencing our tagrte group
  }
}


resource "aws_security_group" "service_security_group" {
  vpc_id      = aws_default_vpc.default_vpc.id

  ingress {
    from_port = 0
    to_port   = 0
    protocol  = "-1"
    # Only allowing traffic in from the load balancer security group
    security_groups = ["${aws_security_group.load_balancer_security_group.id}"]
  }

  egress {
    from_port   = 0 # Allowing any incoming port
    to_port     = 0 # Allowing any outgoing port
    protocol    = "-1" # Allowing any outgoing protocol 
    cidr_blocks = ["0.0.0.0/0"] # Allowing traffic out to all IP addresses
  }
}


# resource "aws_lb_listener_certificate" "lb_cert" {
#   listener_arn    = aws_lb_listener.listener.arn
#   certificate_arn = data.aws_acm_certificate.cert.arn
# }