# A puppet file to install flask:
exec { 'pip3 install flask==2.1.0':
  returns => '0',
}
