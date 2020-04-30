# select os image from docker hub
FROM ubuntu:18.04

# set working directory
#WORKDIR /something

# copy files from where we are to WORKDIR
# COPY . .

# create varible with path
ARG path="/etc/fahclient/"

# url for folding@home .deb file
ARG fold_download_url="https://download.foldingathome.org/releases/public/release/fahclient/debian-stable-64bit/v7.6/fahclient_7.6.9_amd64.deb"
# run command in terminal
# update ubuntu, install wget & dpkg, download folding@home, install folding@home, start folding@home
RUN apt-get update && \
    apt-get install -y wget && \
    apt-get install dpkg && \
    wget -O fold.deb  $fold_download_url && \
    mkdir $path && touch $path/config.xml && \
    dpkg -i --force-depends ./fold.deb


# open port (used to communicate with container)
EXPOSE 1337

# define how to start an application ex. [ "node", "server.js" ]
ENTRYPOINT [ "FAHClient" ]

# The main purpose of a CMD is to provide defaults for executing commands
# source: https://foldingathome.org/support/faq/installation-guides/linux/command-line-options/
CMD [ "--user=Anonymous", "--team=0", "--gpu=false", "--smp=true" ]



# Dockerfile timeline:

# get os (use Debian / Mint / Ubuntu)
# FROM ubuntu: version

# update ubuntu
# sudo apt -get update

# install wget if not already installed
# sudo apt-get install wget

# install dpkg if not already installed
# sudo apt-get install dpkg

# download the folding@home client
# wget -O fold.deb https://download.foldingathome.org/releases/public/release/fahclient/debian-stable-64bit/v7.6/fahclient_7.6.9_amd64.deb

# create structure where config should be located and create config
# mkdir <place_holder> && touch <place_holder>/config.xml

# install the client
# sudo dpkg -i --force-depends ./fold.debd

# to start the client
# sudo /etc/init.d/FAHClient start