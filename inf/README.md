### Quickly creating a new deep learning box
#### Automatic
```
chmod +x setup.sh
./setup.sh
```

#### Manual
```
cd deep-learning
terraform init
terraform apply

# Get your public hostname
terraform show | grep dns

# Edit inventory & add host
vi inventory.yaml

# Configure host
ansible-playbook -i inventory.yaml configure.yml
```
done!
