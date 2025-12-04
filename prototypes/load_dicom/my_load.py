from pyrmifeem.dicom.dicoms import DicomSeriesProcessor
import pyvista as pv

dss=DicomSeriesProcessor("dicoms")
print("Resumen de datos")
print(dss.metadata_summary)

k1=input("Continuar tecla + enter")

dss.quick_preview()

k1=input("Continuar tecla + enter")

dss.quick_preview(len(dss.get_slices)-1)

k1=input("Continuar tecla + enter")

volume_3d = dss.get_volume()

spacing = dss.metadata_summary['spacing']
grid = pv.ImageData() 
grid.dimensions = volume_3d.shape
grid.spacing = (spacing['x'], spacing['y'], spacing['z'])
grid.point_data["values"] = volume_3d.flatten(order="F")

# Visualización interactiva
plotter = pv.Plotter()
plotter.add_volume(grid)#, cmap="gray")#, opacity="sigmoid")
plotter.show()
