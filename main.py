import os
import re



def checkOS():
    """ This finction need from checked OS type and use specific key package manager"""
    fin = open("/etc/os-release", "rt")
    data = fin.read()
    findkey = re.search(
        r'^NAME=\"Arch Linux\"|NAME=\"Debian GNU/Linux\"|NAME=\"Ubuntu GNU/Linux\"|NAME=\"CentOS Linux\"'
        r'|NAME=\"Red Hat Enterprise Linux Server\"', data)
    findresult = findkey.group()
    fin.close()
    key = findresult[5:].replace('"', '')
    return key


def wordpress_docker():

    # Package manager
    keyOS = {
        'Arch Linux': "pacman",
        'Ubuntu GNU/Linux': "apt-get ",
        'Debian GNU/Linux': "apt-get ",
        "CentOS Linux": "yum",
        "Red Hat Enterprise Linux Server": "yum"
    }
    # Specific key from package manager from installation
    installKey = {
        'Arch Linux': "-S --noconfirm",
        'Ubuntu GNU/Linux': "install -y",
        'Debian GNU/Linux': "install -y",
        "CentOS Linux": "install -y",
        "Red Hat Enterprise Linux Server": "install -y"
    }
    # Specific key from package manager from update Repository
    updateKey = {
        'Arch Linux': "-Syu",
        'Ubuntu GNU/Linux': "update",
        'Debian GNU/Linux': "update",
        "CentOS Linux": "update",
        "Red Hat Enterprise Linux Server": "update"
    }
    # Specific key from package manager from remove
    removeKey = {
        'Arch Linux': "-Rs --noconfirm",
        'Ubuntu GNU/Linux': "remove -y",
        'Debian GNU/Linux': "remove -y",
        "CentOS Linux": "remove -y",
        "Red Hat Enterprise Linux Server": "remove -y"
    }
    """MAIN FUNCTION"""
    key_pm = keyOS[checkOS()]
    key_pm_install = installKey[checkOS()]
    key_pm_update = updateKey[checkOS()]
    key_pm_remove = removeKey[checkOS()]
    # install curl and git

    os.system(f" sudo {key_pm} {key_pm_update}")
    os.system(f" sudo {key_pm} {key_pm_install} curl git ")

    # remove old version docker
    os.system(f'sudo {key_pm} {key_pm_remove} docker docker-engine docker.io containerd runc')

    # update package
    os.system(f" sudo {key_pm} {key_pm_update} ")
    os.system(f"sudo {key_pm} {key_pm_install} \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release")

    # download key and add key to apt
    os.system('curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor '
              '-o /usr/share/keyrings/docker-archive-keyring.gpg')

    # add package and repo to apt
    os.system('echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null')

    # install docker
    os.system(f'sudo {key_pm} {key_pm_update} &&'
              f'sudo {key_pm} {key_pm_install} docker-ce docker-ce-cli containerd.io')

    # download docker-compose file
    os.system('sudo curl -L '
              '"https://github.com/docker/compose/releases/download/1.28.6/docker-compose-$(uname -s)-$(uname -m)" '
              '-o /usr/local/bin/docker-compose')

    # add permision to use docker-compose
    os.system('sudo chmod +x /usr/local/bin/docker-compose')

    # create symlimk to /usr/bin/ to use command docker-compose in shell
    os.system('sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose')

    # enable and start daemon docker
    os.system('systemctl start docker && systemctl enable docker')

    # enable current user to docker user no sudo(from secure)
    os.system('usermod -a -G docker $USER &&'
              'systemctl restart docker')
    os.system()


# If this file main run main function as wordpress_docker()
if __name__ == '__main__':
    wordpress_docker()

