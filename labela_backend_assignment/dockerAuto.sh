#bash dockerAuto.sh


echo "Interview project restart docker ............"


# Display Docker images
echo "++++++++++DOCKER IMAGES++++++++++" 
docker images
echo ""
# Rebuild  the Docker Image
docker build -t newcheck:latest .

# Display Docker Containers
echo "++++++++++ALL DOCKER CONTAINERS++++++++++" 
docker ps --all
echo ""


# Stop Docker Containers
echo "++++++++++Stopping DOCKER CONTAINERS++++++++++"
docker stop check
echo ""



# start Docker Containers
echo "++++++++++Restarting DOCKER CONTAINERS++++++++++"
docker start check
echo ""


# Running Docker Containers
echo "++++++++++Running DOCKER CONTAINERS++++++++++"
docker ps