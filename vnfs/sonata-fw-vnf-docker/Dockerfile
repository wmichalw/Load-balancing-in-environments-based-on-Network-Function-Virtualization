FROM ubuntu:xenial
MAINTAINER steven.vanrossem@intec.ugent.be

RUN	apt-get update && apt-get install -y \
	net-tools \
	iproute \
	tcpdump \
	traceroute \
	ethtool \
	python3 \
	python3-pip \
	inetutils-ping \
	vim \
	ifstat

# install OpenvSwitch
RUN apt-get install -y openvswitch-switch openvswitch-common
RUN apt-get upgrade -y openvswitch-switch openvswitch-common
RUN pip3 install ryu
ADD start_fw.sh start.sh
ADD switch_without_learning.py switch_without_learning.py
RUN chmod +x start.sh


# set entry point for emulator gatekeeper
ENV SON_EMU_CMD "./start.sh"

CMD /bin/bash
