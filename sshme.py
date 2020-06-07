#!/usr/bin/python
import sys
import subprocess
import machines

def sshto(m, pkey=None):
	print('Connecting to ' + m[0] + '...')

	if m[2] == '':
		try:
			if pkey != None:
				subprocess.call(['ssh', '-i', pkey, '-l', m[3], m[1]])
			else:
				subprocess.call(['ssh', '-l', m[3], m[1]])
		except KeyboardInterrupt:
			pass
	else:
		try:
			if pkey != None:
				subprocess.call(['ssh', '-i', pkey, '-l', m[3], m[1], '-p', m[2]])
			else:
				subprocess.call(['ssh', '-l', m[3], m[1], '-p', m[2]])
		except KeyboardInterrupt:
			pass

def listall():
	print('Available Servers')
	print('=================')

	for m in machines.hostnames:
		print(m[0], '\t\t', m[1], '\t', m[2], '\t', m[3], '\t', m[4])

	print('')

def listallkeys():
	print('Available Keys')
	print('===============')

	for k in machines.private_keys:
		print(k)
	print()

def main(arg):
	for m in machines.hostnames:
		if arg[0] == 'list':
			listall()
			exit(0)
		elif arg[0] == 'listallkeys':
			listallkeys()
			exit(0)
		elif arg[0] == m[0]:
			if len(m) != 5:
				print('Target found but invalid parameters')
			else:
				if len(arg) == 2 and arg[1] in machines.private_keys:
					sshto(m, pkey=arg[1])
				else:
					sshto(m)
			
			exit(0)
	
	print('Target:', arg[0], 'not found')


def usage():
	print('SSHMe Usage')
	print('-----------')
	print('sshme.py [target-name] [optional:specific key]')
	print('sshme.py listallkeys')
	print('\ntarget-name: The machine\'s name')
	print('[Optional] specific key: If you want to ssh using another key instead of default key')
	print('Specifying target name as \'list\' to list all available servers')
	print('List all keys available in this machine\n')


if __name__ == '__main__':
	if len(sys.argv) == 2 or len(sys.argv) == 3:
		main(sys.argv[1:])
	else:
		usage()