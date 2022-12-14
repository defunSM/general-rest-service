
setup:
	cd app; pip install -r requirements.txt;

# Start virtual environment
env:
	cd app; source .venv/bin/activate;

# Build docker image
build:
	docker build -t dockerimage .

# Run the docker image
run:
	docker run -d -p 3000:3000 dockerimage  

# Test the fastapi on local system
local:
	cd app; uvicorn main:app --reload;

# Check logs for the docker image
logs:
	docker logs myapp

# Removes all previous containers created
clean:
	docker system prune