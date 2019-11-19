import celery

app = celery.Celery('test-celery', broker='redis://localhost', backend='redis://localhost')

if __name__ == "__main__":
    print(app)
