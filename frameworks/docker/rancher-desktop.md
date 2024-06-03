Rancher Desktop
===============

# MacOS

## Administrative right issue with Lima
* Reference:
  https://github.com/rancher-sandbox/rancher-desktop/issues/1811#issuecomment-1561948344
* Work-around
  * Add the following lines, to the `/private/etc/sudoers.d/zzzzz-rancher-desktop-lima` file,
    replacing `<your_user>` by your user name of the MacOS session
    (the `sudo` command will request the user password, in order to escalate administrative rights):
```bash
sudo bash -c 'echo -e "

# Overrides to support starting rancher-desktop after reboot without VPN.
<your_user> ALL=(root:wheel) NOPASSWD:NOSETENV: /bin/mkdir -m 775 -p /private/var/run
<your_user> ALL=(root:wheel) NOPASSWD:NOSETENV: /opt/rancher-desktop/bin/vde_vmne, /usr/bin/pkill -F /private/var/run/*.pid
<your_user> ALL=(daemon:everyone) NOPASSWD:NOSETENV: /opt/rancher-desktop/bin/vde_switch, /usr/bin/pkill -F /private/var/run/*.pid

" >> /private/etc/sudoers.d/zzzzz-rancher-desktop-lima'
```
* During the launch of Rancher Desktop, when Rancher requests the password of the user through a pop window,
  click on the Cancel button rather than on the OK button (otherwise, Rancher Desktop will override the changes
  in the `/private/etc/sudoers.d/zzzzz-rancher-desktop-lima` file)
