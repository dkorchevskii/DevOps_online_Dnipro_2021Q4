provider "aws" {
  region = "eu-central-1"
}

data "aws_ami" "latest_ubuntu" {
  owners      = ["099720109477"]
  most_recent = true
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }
}


resource "aws_instance" "dev_app_server" {
  ami           = data.aws_ami.latest_ubuntu.id
  instance_type = "t2.micro"
  vpc_security_group_ids = [aws_security_group.final-project.id]
  user_data = file("entry-script.sh")

  tags = {
    Environment = "dev"
    Name        = "my dev app server"
    Project     = "Final Project"
  }
}

resource "aws_instance" "prod_app_server" {
  ami           = data.aws_ami.latest_ubuntu.id
  instance_type = "t2.micro"
  vpc_security_group_ids = [aws_security_group.final-project.id]
  user_data = file("entry-script.sh")

  tags = {
    Environment = "prod"
    Name        = "my prod app server"
    Project     = "Final Project"
  }
}



resource "aws_security_group" "final-project" {
  name        = "final project security group"
  description = "final project security group"

  dynamic "ingress" {
    for_each = ["80"]
    content {
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name    = "final project security group"
    Owner   = "Korchevskyi Dmytro"
    Project = "final project"
  }
}



output "dev_app_server_ip" {
  value = aws_instance.dev_app_server.public_ip
}
output "dev_app_server_dns" {
  value = aws_instance.dev_app_server.public_dns
}

output "prod_app_server_ip" {
  value = aws_instance.prod_app_server.public_ip
}
output "prod_app_server_dns" {
  value = aws_instance.prod_app_server.public_dns
}
