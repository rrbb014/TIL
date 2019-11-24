#!/bin/bash

python3 05_celery-chain.py &
celery worker --app 05_celery-chain
