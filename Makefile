setup:
	cd app; pip install -r requirements.txt;

# Start virtual environment
env:
	cd app; source .venv/bin/activate;

# Build docker image
docker:
	docker build -t dockerimage .

# Run the docker image
run:
	docker run -d --name myapp -p 3000:3000 dockerimage  

# Check logs for the docker image
logs:
	docker logs myapp