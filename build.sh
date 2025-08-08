#!/bin/bash

sudo docker login rg.fr-par.scw.cloud/djnd -u nologin -p $SCW_SECRET_TOKEN

# BUILD AND PUBLISH NAJEMNISKI SOS
sudo docker build -f Dockerfile -t najemniski-sos:latest .
sudo docker tag najemniski-sos:latest rg.fr-par.scw.cloud/djnd/najemniski-sos:latest
sudo docker push rg.fr-par.scw.cloud/djnd/najemniski-sos:latest
