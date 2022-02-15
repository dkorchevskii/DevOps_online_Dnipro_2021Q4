#!/bin/bash
sudo apt update && sudo apt install docker.io -y
sudo systemctl start docker
sudo usermod -aG docker ubuntu
docker run -d --rm -p 80:8080 korchevskii/pet-clinic:latest