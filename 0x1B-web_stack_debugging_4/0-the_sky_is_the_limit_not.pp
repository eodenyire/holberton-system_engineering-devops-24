# change data 15 to 10
exec { 'update line':
  cwd => '/etc/default/',
  commnad => '/usr/bin/sudo /bin/sed -i -e "s/15/4096/g" nginx && service nginx restart'
}
#exec { 'restart service':
#  command => '/etc/init.d/nginx restart',
#  path => ['/usr/bin/', '/bin/'],
#}
