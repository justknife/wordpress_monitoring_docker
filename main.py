import os

def wordpress_docker():

    #install curl and git
    os.system(" sudo apt-get update ")
    os.system(" sudo apt-get install -y curl git ")
    #remove old version docker
    os.system('sudo apt-get remove -y docker docker-engine docker.io containerd runc')
    #update package
    os.system(" sudo apt-get update ")
    os.system("sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release")
    #download key and add key to apt
    os.system('curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor '
              '-o /usr/share/keyrings/docker-archive-keyring.gpg')
    #add package and repo to apt
    os.system('echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null')
    #install docker
    os.system('sudo apt-get update &&'
              'sudo apt-get install -y docker-ce docker-ce-cli containerd.io')
    #download docker-compose file
    os.system('sudo curl -L '
              '"https://github.com/docker/compose/releases/download/1.28.6/docker-compose-$(uname -s)-$(uname -m)" '
              '-o /usr/local/bin/docker-compose')
    #add permision to use docker-compose
    os.system('sudo chmod +x /usr/local/bin/docker-compose')
    #create symlimk to /usr/bin/ to use command docker-compose in shell
    os.system('sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose')
    #enable and start daemon docker
    os.system('systemctl start docker && systemctl enable docker')
    #enable current user to docker user no sudo(from secure)
    os.system('usermod -a -G docker $USER &&'
              'systemctl restart docker')
    os.system()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    wordpress_docker()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
