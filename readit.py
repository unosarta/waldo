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

def structure(filename):
	event_log = readit(filename)
	i = 1
	j=1
	sad = {}
	while i <= len(event_log):
		events = []
		while j < len(event_log['particle'+str(i)]):
			dp = event_log['particle'+str(i)][j].split()
			events.append({'cell': dp[1], 'x': dp[2], 'y': dp[3], 'z': dp[4], 'u':dp[5], 'v': dp[6], 'w': dp[7], 'erg' :dp[8], 'wgt':dp[9]})
			j=j+1	
		sad.update({'particle'+str(i): events})		
		i=i+1
	return(sad)

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

def vtk_builder(readable):
	for event_titles in readable:
		vtk_file(readable[event_titles], event_titles)
