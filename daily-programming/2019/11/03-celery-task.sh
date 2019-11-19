#!/bin/bash

python3 celery-task.py &

celery worker --app celery-task
