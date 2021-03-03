from app import app

if __name__ == "__main__":
	app.run()

# to run -> gunicorn --bind 0.0.0.0:8992 wsgi:app -D