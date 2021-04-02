import os
import re
import subprocess

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
    """MAIN FUNCTION"""

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


    key_pm = keyOS[checkOS()]
    key_pm_install = installKey[checkOS()]
    key_pm_update = updateKey[checkOS()]
    key_pm_remove = removeKey[checkOS()]

    # Install curl and git
    try:
        os.system(f" sudo {key_pm} {key_pm_update}")
        os.system(f" sudo {key_pm} {key_pm_install} curl git ")
    except OSError:
        print('Error base installation. Please check your internet connection and try again')

    if checkOS() == 'Arch Linux':

        os.system(f'sudo {key_pm} {key_pm_install} docker')

    else:

        if checkOS() == ('Debian GNU/Linux' or 'Ubuntu GNU/Linux'):

            # remove old version docker
            os.system(f'sudo {key_pm} {key_pm_remove} docker docker-engine docker.io containerd runc')
        else:
            os.system(f'sudo {key_pm} {key_pm_remove} docker \\'
                      f'docker-client \\'
                      f'docker-client-latest \\'
                      f'docker-common \\'
                      f'docker-latest \\'
                      f'docker-latest-logrotate \\'
                      f'docker-logrotate \\'
                      f'docker-engine')

        # Update package
        os.system(f" sudo {key_pm} {key_pm_update} ")

        if checkOS() == ('Debian GNU/Linux' or 'Ubuntu GNU/Linux'):

            # Install dependencies docker
            os.system(f"sudo {key_pm} {key_pm_install} \
                 apt-transport-https \\"
                      f"ca-certificates \\"
                      f"gnupg \\"
                      f"lsb-release")
            # Download key and add key to apt
            os.system('curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor '
                      '-o /usr/share/keyrings/docker-archive-keyring.gpg')

            # Add package and repo to apt
            os.system('echo \
          "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian \
          $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null')

        elif checkOS() == ('Red Hat Enterprise Linux Server' or 'CentOS Linux'):

            os.system(f'sudo {key_pm} {key_pm_install} yum-utils')
            os.system('sudo yum-config-manager \\'
                      '--add-repo \\'
                      'https://download.docker.com/linux/centos/docker-ce.repo')

        # Install docker
        os.system(f'sudo {key_pm} {key_pm_update} &&'
                  f'sudo {key_pm} {key_pm_install} docker-ce docker-ce-cli containerd.io')

        # Enable and start daemon docker
        os.system('systemctl start docker && systemctl enable docker')

        # Enable current user to docker user no sudo(from secure)
        os.system('usermod -a -G docker $USER &&'
                  'systemctl restart docker')

    # Download docker-compose file
    uname_s = subprocess.Popen(f"uname -s", shell=True, stdout=subprocess.PIPE)
    uname_s = uname_s.stdout.read()
    uname_s = uname_s[:-1]
    uname_s = uname_s.decode('utf-8')
    uname_m = subprocess.Popen(f"uname -m", shell=True, stdout=subprocess.PIPE)
    uname_m = uname_m.stdout.read()
    uname_m = uname_m[:-1]
    uname_m = uname_m.decode('utf-8')
    os.system(f'sudo curl -L "https://github.com/docker/compose/releases/download/1.28.6/docker-compose-{uname_s}-'
              f'{uname_m}" '
              f'-o /usr/local/bin/docker-compose')

    # Add permision to use docker-compose
    os.system('sudo chmod +x /usr/local/bin/docker-compose')

    # Create symlimk to /usr/bin/ to use command docker-compose in shell
    os.system('sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose')
    os.system('mkdir -p data/html')
    os.system('mkdir -p data/prometheus')
    os.system('mkdir -p grafana/provisioning')


# If this file main run main function as wordpress_docker()
if __name__ == '__main__':
    wordpress_docker()
