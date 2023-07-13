# Image Transfer Code
This is a sample code for image transfer from client to server.

## Prerequistes
* Python
* Docker

## How to Start it
### Easy to start
1. Firstly, please install the dependency packages by `pip install -r requirements.txt`
2. You need to customize to setup the client and server address.
3. And please setup your directory path of images in `load_bullets({your path})`.
4. Then `round_shoot` is that the program sends the data automatically; `shoot` is that the program sends the data on your control.

### Container requirement
If you would like to run the program in a container. There is the dockerfiles `image_client_Dockerfile` and `image_server_DOckerfile` for client and server, respectively.

1. Please first to build the dockerfile into image. The example of command: `docker build -f image_client_Dockerfile -t {tag name/image name} .`.

2. And then start the container. e.g., `docker run -p 8888:8888 -d {image name:tag}`

### Debug functions
* In the `channel_server_api.py`, the function `__write_file` is for debugging, so if you don't use this function, you can remove or comment it.
* The `written_img` directory is the place where `__write_file` writes the image files.

## Running Snapshot
Transfer the images between host and raspberry pi (OS: ubuntu 22.04).
* Running without container

![Hosts_Start](https://github.com/ImStudyingProgrammer/Image_Transfer_Code/assets/Hosts_20230713_183802.png =480x240)
![Hosts_Image_Transfer](https://github.com/ImStudyingProgrammer/Image_Transfer_Code/assets/Hosts_20230713_183846.png =480x240)

* Running with container

![Containers_Start](https://github.com/ImStudyingProgrammer/Image_Transfer_Code/assets/Containers_20230713_184110.png =480x240)
![Containers_Server_Logs](https://github.com/ImStudyingProgrammer/Image_Transfer_Code/assets/Containers_20230713_184138.png =480x240)
![Containers_Images_In_Server](https://github.com/ImStudyingProgrammer/Image_Transfer_Code/assets/Containers_20230713_184202.png =480x240)



