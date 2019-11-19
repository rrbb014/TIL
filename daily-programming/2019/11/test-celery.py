import celery

app = celery.Celery('test', broker='redis://localhost', backend='redis://localhost')

if __name__ == "__main__":
    print(app)
