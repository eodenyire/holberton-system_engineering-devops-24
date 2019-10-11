# change data 15 to 10
exec { 'update line':
  commnad => '/usr/bin/sudo /bin/sed -i -e "s/\-n 15/\-n 10240/g" /etc/default/nginx && service nginx restart'
}
#exec { 'restart service':
#  cwd => '/etc/default/',
#  command => '/etc/init.d/nginx restart',
#  path => ['/usr/bin/', '/bin/'],
#}
#
#xx -n 10000
