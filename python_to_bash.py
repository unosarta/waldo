import modules as m

filename = input('Please name the MCNP file to be made into VTK format: ')

readable = m.structure(filename)
vtk_contents = m.vtk_builder(readable)
