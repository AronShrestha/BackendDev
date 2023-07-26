
## Monolith

Monolith can be a large codebase with different functionality and  that is connected with a single big database.
![[m1.png]]


In this example , we have search func that can have a lot of traffic , etc and contact page with less traffic.
If we want to scale this app because of huge traffic in search functionality we have to replicate all the functionality like we need also replicate those functionality that doesn't have traffic #b bam (waste of resource) .There will only be one repository that so changing language and code can affect.

## Microservice 

They are smaller independent services that have their own independent database and they can communicate with eachother using event pass.
Advantage :1) we can scale based on traffic so if we see search service we can scale 4 times but we don;t now need to scale contact that has no traffic.
2) Seperation of concern : now product recomendation team can only focus on ML not about scaling.
3) Can use different programming language according to use.


 ![[m2.png]]


# Architecture of App we are building
 ![[m3.png]] 



## All about dockerfile and docker

### Dockerfile : 

a) base image
b) environment variables [useful to get log]
c) We then specify the working directory (as WORKDIR /app)
d) Then we will copy requirement.txt from  our project to working directory we that we made above.(i.e copying inside docker container)
e) then we will install requirements.txt that will install all requirements in the requirement.txt file

f)then we copy all the file of our project  to app directory (as COPY . /app)
g) We will write command to run the project

### Docker-compose file
1) we start by adding the version 
2) and then we will specify the services
3)  like in example we have added a backend service
4) first we need to specify the dockerfile (build:)
5) we then do context : . (here this specify this folder)
6) we give docker file as dockerfile : Dockerfile(name of dockerfile)
7) then we need to specify the port :this port that is running here, is inside the docker container is not our localhost .
So we need to tell localhost to listen to specific port **''i.e localhostport : dockerfileport(i.e port inside the container)''**
9) volumes :  
		- . : /app (this means all the file contained here in project are connected with docker container. Everytime i make changes in project will pass it to the container and vice-versa)

#### Database config in django 
'HOST': 'service name ' like db in below exampleD![[m4.png]]
port : port inside this service i.e inside the container here 3306

## Docker commands

To go inside the docker container:
command is : docker-compose exec %nameoftheservice  sh
example from above docker file :
docker-compose exec backend sh

