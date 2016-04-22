import pdb
def readit(filename):

	data = open(filename, 'r+')
	line = data.readline()
	i=1
	event_log = {}
	while line != '':
		if 'event' in line:
			line = data.readline()
			line = data.readline()
			line = data.readline()
			line = data.readline()
			event = []
			while (line.find('event') == -1) & (line.find('summary') == -1):
				event.append(line)
				line = data.readline()
			if event != []:
				event_log.update({'particle'+str(i) : event})			
			i=i+1
		else: line = data.readline() 
	return event_log

