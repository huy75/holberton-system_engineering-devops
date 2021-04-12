# This manifest installs nginx and adds redirect page, custome header

exec { 'update':
     command => '/usr/bin/apt-get update',
}

package {'nginx':
  ensure => present,
  name   => 'nginx',
}

file {'/var/www/html/index.html':
  ensure  => present,
  path    => '/var/www/html/index.html',
  content => 'Holberton School for the win!',
}

file_line { 'redirect_me':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

file_line { 'cstHeader':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'add_header X-Served-By $hostname;',
}

service { 'nginx':
  ensure     => running,
  require    => Package['nginx'],
}