#!/bin/bash

cd src/
docker-compose build
docker-compose up --detach
