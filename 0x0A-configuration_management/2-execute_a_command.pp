# A puppet file to kill a process calles killmenow
exec { 'pkill -9 killmenow'
  path    => 'usr/local/bin:/usr/bin:/usr/sbin:/bin'
  returns => '0',
}
