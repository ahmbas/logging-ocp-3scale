FROM centos:7


RUN yum install -y wget
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python get-pip.py
RUN pip install requests python-dateutil

COPY cleanup.py cleanup.py
ENTRYPOINT ["/usr/bin/python", "cleanup.py"]
