provider "aws" {
  region = "us-west-2"
}

resource "aws_security_group" "allow_ssh_ephemeral_ingress" {
  name        = "allow_ssh"
  description = "allows ingress of ssh traffic"
  
  ingress {
    from_port = 22
    to_port   = 22
    protocol  = "tcp"
    # Allow access from anywhere - you can restrict this to specific IPs (recommended)
    cidr_blocks = ["0.0.0.0/0"] 
  }

  # ephemeral ingress ports are required for updates / pip 
  ingress {
    from_port = 32768 
    to_port   = 65535
    protocol  = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port = 0
    to_port   = 0 
    protocol  = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
  
resource "aws_instance" "deep-learning" {
  ami           = "ami-0688c8f24f1c0e235"
  instance_type = "p2.xlarge"
  key_name      = "erik-deep-learning"
  security_groups = ["allow_ssh"]
}
