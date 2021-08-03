#!/bin/bash

sudo docker login rg.fr-par.scw.cloud/djnd -u nologin -p $SCW_SECRET_TOKEN

# BUILD AND PUBLISH NAJEMNISKI SOS
sudo docker build -f stanovanja/Dockerfile -t stanovanja:latest .
sudo docker tag stanovanja:latest rg.fr-par.scw.cloud/djnd/stanovanja:latest
sudo docker push rg.fr-par.scw.cloud/djnd/stanovanja:latest
