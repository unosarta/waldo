import pdb
import itertools as it

def scinot(string):
	"""Takes a string in MCNP scientific notation (without 'E' character), and returns a string of standard scientific notation."""
	"""If there is no '+' or '-' character in string, returns it as it is."""
	"""If the argument is not string, returns the argument"""
	if type(string) != str:
		return string
	else:
		retstr = string[0]
		for char in string[1:]:
			if ((char == '-')|(char == '+')):
				retstr += 'E' + char
			else:
				retstr += char
		
		return retstr


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
	particle_data = readit(filename)

	event_log = {}
	for elog in particle_data:
		event_log[elog] = []
		for line in particle_data[elog]:
			dp = line.split()
			event = {}
			event.update({'int': scinot(dp[0])})
			event.update({'cell': scinot(dp[1])})
			event.update({'x': scinot(dp[2])})
			event.update({'y': scinot(dp[3])})
			event.update({'z': scinot(dp[4])})
			event.update({'u': scinot(dp[5])})
			event.update({'v': scinot(dp[6])})
			event.update({'w': scinot(dp[7])})
			event.update({'erg': scinot(dp[8])})
			event.update({'wgt': scinot(dp[9])})
			event_log[elog].append(event)
	return(event_log)

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
	vtk_file.write("CELL_DATA 1\n")
	vtk_file.write("POINT_DATA " + str(num_events) + "\n")
	vtk_file.write("scalars pointvar float\nLOOKUP_TABLE default\n")
	vtk_file.write("1.2 1.3 1.4 1.5")

def vtk_builder(readable):
	for event_titles in readable:
		vtk_file(readable[event_titles], event_titles)
