import readit as r

filename = input('Please name the MCNP file to be made into VTK format: ')
newfile = input('Please name the VTK output file: ')
vtk_file = open(str(newfile)+'.vtk', '+w')

readable = r.structure(filename)
vtk = vtk_builder(readable)
vtk_file.write(str(vtk))	


