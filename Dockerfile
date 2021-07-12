FROM mengkevin/miniconda3:4.7.12

# Install numpy using system package manager
RUN apt-get -y update && apt-get -y install ffmpeg imagemagick 
# && apt-get install -y build-essential

# Install some special fonts we use in testing, etc..
RUN apt-get -y install fonts-liberation


RUN apt-get install -y locales && \
    locale-gen C.UTF-8 && \
    /usr/sbin/update-locale LANG=C.UTF-8

ENV LC_ALL C.UTF-8

# ADD . /var/src/moviepy/
RUN git clone https://github.com/Zulko/moviepy.git /var/src/moviepy
RUN cd /var/src/moviepy/ && pip install .[optional]

# install npm
RUN apt-get install npm && npm -g install npm && npm install -g cnpm --registry=https://registry.npm.taobao.org && \
    npm install -g @vue/cli 


# modify ImageMagick policy file so that Textclips work correctly.
RUN sed -i 's/none/read,write/g' /etc/ImageMagick-6/policy.xml 

# FOR flask
EXPOSE 5000
EXPOSE 8080
EXPOSE 8081
EXPOSE 3306
