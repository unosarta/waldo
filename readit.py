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

def file_struct(event_log):

	ready_for_vtk = {}
	for particle in event_log:
		ready_for_vtk[particle] = []
		for event in event_log[particle]:
			list = event.split()
			ready_for_vtk[particle].append({})
			ready_for_vtk[particle][event_log[particle].index(event)]['something'] = list[0]
			ready_for_vtk[particle][event_log[particle].index(event)]['cell'] = list[1]
			ready_for_vtk[particle][event_log[particle].index(event)]['x'] = list[2]
			ready_for_vtk[particle][event_log[particle].index(event)]['y'] = list[2]
			ready_for_vtk[particle][event_log[particle].index(event)]['z'] = list[3]
			ready_for_vtk[particle][event_log[particle].index(event)]['u'] = list[4]
			ready_for_vtk[particle][event_log[particle].index(event)]['v'] = list[5]
			ready_for_vtk[particle][event_log[particle].index(event)]['w'] = list[6]
			ready_for_vtk[particle][event_log[particle].index(event)]['erg'] = list[7]
			ready_for_vtk[particle][event_log[particle].index(event)]['wgt'] = list[8]
	return ready_for_vtk
