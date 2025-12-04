import pydicom
from pydicom.pixel_data_handlers.util import apply_voi_lut
import matplotlib.pyplot as plt

# Cargar archivo DICOM
ds = pydicom.dcmread("./dicoms/localizer_i10.dcm")
print(ds.SliceLocation)
print(ds.ImagePositionPatient) 

# Aplicar ajustes de ventana (VOI LUT)
img = apply_voi_lut(ds.pixel_array, ds)

# Visualización básica con matplotlib
plt.imshow(img,)# cmap="gray") # Escala de grices 
plt.axis("off")
plt.show()
