FROM ghcr.io/linuxserver/code-server:version-v3.8.0 as builder


# RUN apt-get update -qq; apt-get install -y -qq bash zsh htop python3-pip zip unzip apache2-utils nmap iputils-ping iproute2 && rm -rf /tmp/**

RUN apt-get update -qq; apt-get install -y -qq bash zsh htop python3-pip zip unzip iputils-ping ca-certificates && rm -rf /tmp/**
# RUN apt-get update -qq; apt-get install -y -qq php-cli php-opcache php-zip php-curl php-yaml php-phpdbg php-xml php-mbstring php-curl php-zip php-pdo-sqlite php-intl php-zmq && rm -rf /tmp/**

# Dependencies for markdown pdf export
# RUN apt-get update -qq && apt-get install libxcomposite1 libxdamage1 libxtst6 libnss3 libcups2 libxss1 libasound2 libatk1.0-0 libatk-bridge2.0-0 libgtk-3-0 -y --no-install-recommends && rm -rf /tmp/**
# RUN apt-get update -qq && apt-get install openbox -y --no-install-recommends && rm -rf /tmp/**

RUN pip3 install jupyter
# RUN pip3 install ipython
# RUN pip3 install notebook
# RUN pip3 install jupyterlab 
RUN pip3 install docker-compose

RUN pip3 install bash_kernel
RUN python3 -m bash_kernel.install

RUN pip3 install sshkernel
RUN python3 -m sshkernel install 


RUN url=https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && tmp="$(mktemp)" \
    && curl -L "$url" >> "$tmp" \
	&& sudo dpkg -i "$tmp" \
	; sudo apt install -f -y -qq \
    && rm "$tmp"

SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

# RUN apk add --no-cache docker curl
RUN curl -SsL https://get.docker.com | bash -
RUN curl -SsL https://raw.githubusercontent.com/moby/moby/master/hack/dind > /bin/dind && chmod +x /bin/dind
RUN mkdir -p /etc/services.d/dind && printf '#!/usr/bin/execlineb -P\ndind dockerd\n' >> /etc/services.d/dind/run && chmod +x /etc/services.d/dind/run

ENV PUSER mandy

RUN usermod -aG docker abc
RUN chsh -s $(which bash) abc

RUN usermod -l $PUSER abc
RUN usermod -d /home/$PUSER -m $PUSER
RUN groupmod -n $PUSER abc
ENV SHELL zsh
RUN chsh -s $(which zsh) $PUSER


RUN npm install -g --silent --force json

RUN apt-get update -qq; apt-get install -y -qq vim && rm -rf /tmp/**

RUN sudo sh -c 'curl -s https://raw.githubusercontent.com/BorisWilhelms/devcontainer/main/devcontainer.sh > /usr/local/bin/devcontainer && chmod +x /usr/local/bin/devcontainer'
COPY ./code/services.d/ /etc/services.d/
COPY ./code/cont-init.d/ /etc/cont-init.d/



RUN grep -R -l abc /etc/cont-init.d | xargs sed -i "s/abc/$PUSER/g"
RUN grep -R -l abc /etc/services.d | xargs sed -i "s/abc/$PUSER/g"
ENV HOME /home/$PUSER


RUN chown $PUSER:$PUSER -R /home/$PUSER
RUN rm -rf /config && ln -fs /home/$PUSER /config



FROM builder as kubernetes


RUN curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.9.0/kind-linux-amd64 && chmod +x ./kind && mv ./kind /bin/kind

# https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/
RUN apt-get update && sudo apt-get install -y apt-transport-https curl
RUN curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
RUN echo 'deb https://apt.kubernetes.io/ kubernetes-xenial main' | sudo tee /etc/apt/sources.list.d/kubernetes.list
RUN apt-get update && apt-get install -y kubelet kubeadm kubectl && apt-mark hold kubelet kubeadm kubectl

COPY ./kubernetes/services.d/ /etc/services.d/



FROM builder as code