# wordpress wp-settings.php
exec { 'remove type phpp to php':
    cwd     => '/var/www/html',
    command => '/bin/sed -i -e "s/.phpp/.php/g" wp-settings.php',
}
