# Changing the OS configuration to be able to login with the holberton user and open a file without any error message.
exec { 'os_conf':
  path    => '/usr/bin:/usr/sbin:/bin',
  command => 'sed -i -e "s/nofile 5/nofile 5000/g" /etc/security/limits.conf;
  sed -i -e "s/nofile 4/nofile 4000/g" /etc/security/limits.conf'
}
