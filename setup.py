import os

distro = raw_input("1: Debian, 2: Fedora, 3: Arch")
pkg_cmd = {
"1":"apt-get install zsh i3"
"2":"dnf install zsh i3"
"3":"pacman -S zsh i3-wm"
}.get(distro, "apt-get install zsh i3")

os.system("sudo {}".format(pkg_cmd))
