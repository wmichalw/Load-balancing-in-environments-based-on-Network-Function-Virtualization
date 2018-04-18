FROM ubuntu:xenial

ENV IFIN input
ENV IFOUT output

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
RUN pip3 install asyncio
RUN pip3 install requests
RUN pip3 install aiohttp

ADD ovs.sh ovs.sh
ADD start_load_balancer.sh start_load_balancer.sh
ADD restart.sh restart.sh
ADD load_balancer.py load_balancer.py
ADD kill.sh kill.sh

RUN chmod +x ovs.sh
RUN chmod +x start_load_balancer.sh
RUN chmod +x restart.sh
RUN chmod +x kill.sh

# set entry point for emulator gatekeeper
ENV SON_EMU_CMD "./start_load_balancer.sh"

CMD /bin/bash
