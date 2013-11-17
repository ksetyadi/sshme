#!/usr/bin/python
import sys
import subprocess
import machines

def sshto(m):
	print 'Connecting to ' + m[0] + '...'

	if m[2] == '':
		try:
			subprocess.call(['ssh', '-l', m[3], m[1]])
		except KeyboardInterrupt:
			pass
	else:
		try:
			subprocess.call(['ssh', '-l', m[3], m[1], '-p', m[2]])
		except KeyboardInterrupt:
			pass


def main(arg):
	for m in machines.hostnames:
		if arg[0] == m[0]:
			if len(m) != 4:
				print 'Target found but invalid parameters'
			else:
				sshto(m)
			
			exit(0)
	
	print 'Target:', arg[0], 'not found'


def usage():
	print 'SSHMe Usage'
	print '-----------'
	print 'sshme.py [target-name]'
	print '\ntarget-name: The machine''s name\n'


if __name__ == '__main__':
	if len(sys.argv) == 2:
		main(sys.argv[1:])
	else:
		usage()