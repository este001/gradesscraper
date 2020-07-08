FROM selenium/standalone-chrome

USER root
RUN sudo apt update
RUN sudo apt install python3-pip -y
COPY . /opt/
WORKDIR /opt
RUN sudo pip3 install -r requirements.txt
RUN python3 test_scrape.py;exit 0
