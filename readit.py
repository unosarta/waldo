import pdb
import itertools as it
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

def vtk_file(events, event_title):

	file_name = event_title + ".vtk"
	vtk_file = open(file_name,"w+")
	num_events = 0
	for event in events:
		if event["cell"] != events[events.index(event)-1]["cell"]:
			num_events += 1
	vtk_file.write("# vtk DataFile Version 3.0 \nvtk output\nASCII\nDATASET POLYDATA\nPOINTS " + str(num_events) + " float\n")
	for event in events:
		if event["cell"] != events[events.index(event)-1]["cell"]:
			vtk_file.write(event["x"] + " " + event["y"] + " " + event["z"] + "\n")
	num_lines = num_events - 1
	vtk_file.write("LINES " + str(num_lines) + " " + str(3*num_lines) + "\n")
	for i in range(num_events-1):
		vtk_file.write("2 " + str(i) + " " + str(i+1) + "\n")
	vtk_file.write("CELL_DATA " + str(num_lines) + "\n")
	vtk_file.write("scalars cellvar float\nLOOKUP_TABLE default\n")
	vtk_file.write("2.0 2.4 2.1 2.2 2.3\n")
	vtk_file.write("POINT_DATA " + str(num_events) + "\n")
	vtk_file.write("scalars pointvar float\nLOOKUP_TABLE default\n")
	vtk_file.write("1.2 1.3 1.4 1.5")
