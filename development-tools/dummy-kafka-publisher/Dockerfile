FROM centos:7

# Install python
RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm &&\
  yum -y update
RUN yum install -y gcc python36u python36u-devel python36u-pip
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.6 1 &&\
  update-alternatives --install /usr/bin/pip pip /usr/bin/pip3.6 1

# Install requirements
WORKDIR /usr/src/antenna-pad-publisher
COPY requirements.txt .
RUN pip install -r requirements.txt

# Expose port
EXPOSE 8001

COPY entrypoint.sh .
COPY . .
ENTRYPOINT ["./entrypoint.sh"]
