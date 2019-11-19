#!/bin/bash

python3 06_celery-task-queue.py &
celery worker --app 06_celery-task-queue --queues celery,low-priority

