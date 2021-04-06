# This manifest installs ngix and adds redirect page

package { 'nginx':
  ensure => present,
  name   => 'nginx',
}

file { '/usr/share/nginx/html/index.html':
  ensure  => present,
  path    => '/usr/share/nginx/html/index.html',
  content => 'Holberton School for the win!',
}

file_line { 'redirect':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  require    => Package['nginx'],
  subscribe  => File_line['redirect_me'],
}