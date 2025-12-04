import pydicom
import numpy as np
import matplotlib.pyplot as plt
import os


class DicomSeriesProcessor:
    def __init__(self, dicom_dir: str):
        """
        Inicializa el procesador de series DICOM
        :param dicom_dir: Ruta absoluta al directorio con archivos .dcm
        """
        self.dicom_dir = dicom_dir
        self.slices = []
        self._load_and_validate()
        self._sort_slices()

    def _load_and_validate(self):
        """Carga y valida los archivos DICOM"""
        required_tags = ['ImagePositionPatient',
                         'ImageOrientationPatient', 'PixelSpacing']

        for filename in os.listdir(self.dicom_dir):
            if not filename.endswith('.dcm'):
                continue

            try:
                filepath = os.path.join(self.dicom_dir, filename)
                ds = pydicom.dcmread(filepath, stop_before_pixels=False)

                # Validación de metadatos críticos
                if not all(hasattr(ds, tag) for tag in required_tags):
                    raise ValueError(
                        f"Archivo {filename} carece de metadatos esenciales")

                self.slices.append(ds)

            except Exception as e:
                print(f"Error cargando {filename}: {str(e)}")
                continue

    def _sort_slices(self):
        """Ordena los slices usando ImagePositionPatient (coordenada Z)"""
        if not self.slices:
            raise ValueError("No hay slices válidos para ordenar")

        # Verificar consistencia de orientación y espaciado
        ref_orientation = self.slices[0].ImageOrientationPatient
        ref_spacing = self.slices[0].PixelSpacing

        for slice in self.slices[1:]:
            if (slice.ImageOrientationPatient != ref_orientation or
                    slice.PixelSpacing != ref_spacing):
                raise ValueError(
                    "Inconsistencia en orientación o espaciado entre slices")

        # Ordenar por posición en eje Z (tercer elemento de ImagePositionPatient)
        self.slices.sort(key=lambda x: float(x.ImagePositionPatient[2]))

    def get_volume(self) -> np.ndarray:
        """Devuelve el volumen 3D como array numpy"""
        return np.stack([s.pixel_array for s in self.slices], axis=0)

    def get_slice(self, index: int) -> np.ndarray:
        """Obtiene un slice específico con validación de índices"""
        if index < 0 or index >= len(self.slices):
            raise IndexError(
                f"Índice {index} fuera de rango [0-{len(self.slices)-1}]")
        return self.slices[index].pixel_array

    @property
    def metadata_summary(self) -> dict:
        """Resumen de metadatos comunes"""
        if not self.slices:
            return {}

        first_slice = self.slices[0]
        return {
            'modality': getattr(first_slice, 'Modality', 'Desconocido'),
            'patient_id': getattr(first_slice, 'PatientID', 'N/A'),
            'spacing': {
                'x': float(first_slice.PixelSpacing[0]),
                'y': float(first_slice.PixelSpacing[1]),
                'z': abs(float(self.slices[1].ImagePositionPatient[2]) -
                         float(self.slices[0].ImagePositionPatient[2]))
            },
            'dimensions': {
                'x': first_slice.Columns,
                'y': first_slice.Rows,
                'z': len(self.slices)
            }
        }

    def quick_preview(self, slice_index=0):
        """Muestra un preview matplotlib del slice"""
        plt.imshow(self.get_slice(slice_index), cmap='gray')
        plt.title(f"Slice {slice_index}")
        plt.axis('off')
        plt.show()
