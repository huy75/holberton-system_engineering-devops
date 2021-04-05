# This manifest installs ngix and adds redirect page

$command = "/usr/bin/env sed -i '/listen 80 default_server;/a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;' /etc/nginx/sites-available/default"

package { 'nginx':
  ensure   => 'installed',
  provider => 'nginx'
}

file { '/usr/share/nginx/html/index.html':
  ensure  => file,
  path    => '/usr/share/nginx/html/index.html',
  content => 'Holberton School for the win!'
}

exec { '301 redirect':
  command => $command
}

service { 'nginx':
  ensure  => 'running',
  restart => 'sudo service nginx restart'
}