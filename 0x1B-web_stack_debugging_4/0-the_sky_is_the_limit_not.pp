# increasing amount of HTTP requests to a web server
exec { 'u_limit':
  path    => '/usr/bin:/usr/sbin:/bin',
  command => 'sed -i -e "s/15/4096/g" /etc/default/nginx; service nginx restart'
}
