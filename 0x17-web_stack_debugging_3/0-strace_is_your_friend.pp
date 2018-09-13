# find out why Apache is returning a 500 error
exec { 'fix_the_prosecc':
  command => 'sed -i -e "s/class-wp-locale.phpp/class-wp-locale.php/g" /var/www/html/wp-settings.php',
  provider => 'shell'
}
