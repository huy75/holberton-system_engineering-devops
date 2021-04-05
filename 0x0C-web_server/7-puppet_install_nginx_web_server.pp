# This manifest installs ngix and adds redirect page

package { 'nginx':
  ensure => installed,
  name   => 'nginx'
}

file { '/usr/share/nginx/html/index.html':
  path    => '/usr/share/nginx/html/index.html',
  content => 'Holberton School for the win!'
}

file_line { 'Redirection, 301':
  path     => '/etc/nginx/sites-available/default',
  ensure   => 'present',
  after    => 'server_name _;',
  line     => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  multiple => true
}

service { 'nginx':
  ensure  => 'running',
  require => Package['nginx']
}