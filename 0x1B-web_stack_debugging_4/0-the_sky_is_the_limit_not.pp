# change data 15 to 10
exec { 'update line':
  cwd => '/etc/default/',
  path => ['/usr/bin/', '/bin/'],
  commnad => 'sed -i "s/15/4096/g && service nginx restart"'
}
#exec { 'restart service':
#  command => '/etc/init.d/nginx restart',
#}
