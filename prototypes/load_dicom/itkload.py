import SimpleITK as sitk
import matplotlib.pyplot as plt

# Leer serie DICOM
reader = sitk.ImageSeriesReader()
dicom_series = reader.GetGDCMSeriesFileNames("./dicoms")
reader.SetFileNames(dicom_series)
image = reader.Execute()

# Convertir a array de numpy
img_array = sitk.GetArrayFromImage(image)

# Visualizar slice central (ej: tomografía)
slice_idx = img_array.shape[0] // 2
plt.imshow(img_array[slice_idx])#, cmap="gray")
plt.show()
