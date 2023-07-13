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

![Hosts_20230713_183802](https://github.com/ImStudyingProgrammer/Image_Transfer_Code/assets/25094738/f7e5304c-3f37-4adb-83cc-794212e1c48f =480x240)
![Hosts_20230713_183846](https://github.com/ImStudyingProgrammer/Image_Transfer_Code/assets/25094738/2ac45cfd-6822-4a7c-8e71-f95e93618fcf)
* Running with container

![Containers_20230713_184110](https://github.com/ImStudyingProgrammer/Image_Transfer_Code/assets/25094738/a3a77125-11b8-4327-adb4-29bf87ffcebd)
![Containers_20230713_184138](https://github.com/ImStudyingProgrammer/Image_Transfer_Code/assets/25094738/0030fe1e-073b-45ee-bf1f-91d9965b5d0e)
![Containers_20230713_184202](https://github.com/ImStudyingProgrammer/Image_Transfer_Code/assets/25094738/2c133417-060e-433c-a030-113e423eee71)



