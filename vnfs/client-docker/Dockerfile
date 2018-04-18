FROM ubuntu:xenial
MAINTAINER manuel.peuster@uni-paderborn.de

RUN	apt-get update && apt-get install -y \
	net-tools \
	iproute \
	tcpdump \
	curl \
	vim \
	inetutils-ping \
	iperf3 \
	netcat \
	nmap \
	ethtool \
	apache2-utils \
	ssh

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python get-pip.py
RUN pip install requests statistics

ADD start.sh start.sh
RUN chmod +x start.sh
# set entry point for emulator gatekeeper
ENV SON_EMU_CMD "./start.sh"

CMD /bin/bash
