#!/bin/bash

python3 04_celery-task-retry.py &
celery worker --app 04_celery-task-retry
