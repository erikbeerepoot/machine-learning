#!/bin/bash
# Script to automatically configure a new ec2 box end-to-end

# Setup new ec2 instance (or change existing)
terraform apply -auto-approve

# Delete existing hosts from inventory
sed '/ec2.*\.compute\.amazonaws\.com/d' inventory.yaml > temp.inventory 
mv temp.inventory inventory.yaml 

# Add host from terraform 
terraform show | grep public_dns | awk '/public_dns =/ { print $3 }' >> inventory.yaml

# Configure ec2 instance
ansible-playbook -i inventory.yaml configure.yml
