#!/bin/bash

docker-compose exec django python manage.py dumpdata problems --indent 2 --exclude problems.Submission --output lovelace_problems.json
