# find out why Apache is returning a 500 error
exec { 'fix_the_prosecc':
  path => '/usr/bin:/usr/sbin:/bin',
  provider => 'shell',
  command => 'sed -i -e "s/class-wp-locale.phpp/class-wp-locale.php/g" /var/www/html/wp-settings.php'
}
