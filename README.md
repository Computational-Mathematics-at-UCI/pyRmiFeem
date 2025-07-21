# PyRMIFEEM

Python toolkit para construir y visualizar modelos por Elementos Finitos (FEM) de tejido y estructuras óseas a partir de imágenes de Resonancia Magnética (RMI) almacenadas en ficheros DICOM. Se apoya en FEBio vía el binding `febio-python` y en librerías de preprocesado, segmentación, mallado y visualización.

---

## Características

- Lectura y preprocesado de volúmenes DICOM
- Segmentación semiautomática de hueso y tejidos blandos  
- Generación de mallas 3D a partir de máscaras segmentadas  
- Simulación FEM con FEBio (hiperelástico, poroelástico, viscoelástico)  
- Visualización interactiva de mallas y resultados con PyVista  

---

## Requisitos previos

1. Python 3.8 o superior  
2. FEBio 3.x instalado y accesible en tu sistema  
   - Define la variable de entorno `FEBIO_HOME` apuntando al directorio de FEBio  
3. CMake, compiladores de C/C++ (solo si deseas compilar FEBio desde fuente)  

---

## Instalación

1. Clona este repositorio  
   ```bash
   git clone https://github.com/tu-usuario/pyrmifeem.git
   cd pyrmifeem
   ```

2. Crea un entorno virtual e instala dependencias  
   ```bash
   python3 -m venv venv
   source venv/bin/activate        # Linux/macOS
   .\venv\Scripts\activate         # Windows PowerShell
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. Comprueba que FEBio está disponible  
   ```bash
   echo $FEBIO_HOME                # Linux/macOS
   echo %FEBIO_HOME%               # Windows
   ```

---

## Estructura del proyecto

```text
pyrmifeem/
├── examples/               
│   └── pipeline.py         # Script de ejemplo que recorre todo el workflow
├── pyrmifeem/
│   ├── io.py               # Lectura DICOM y volúmenes
│   ├── segmentation.py     # Funciones de segmentación
│   ├── meshing.py          # Extracción y refinado de mallas
│   ├── simulation.py       # Interfaces a febio-python
│   └── visualization.py    # Scripts de visualización con PyVista
├── requirements.txt        # Librerías Python
├── README.md
└── LICENSE                 # MIT License
```

---

## Uso básico

```python
from pyrmifeem.io import load_dicom_series
from pyrmifeem.segmentation import segment_bone
from pyrmifeem.meshing import marching_cubes_to_mesh
from pyrmifeem.simulation import FebioSimulation
from pyrmifeem.visualization import show_mesh

# 1. Carga RMI desde DICOM
volume, spacing = load_dicom_series("datos/paciente01/DICOM/")

# 2. Segmenta hueso y tejido
mask_bone = segment_bone(volume, method="otsu")

# 3. Genera malla de superficie
vertices, faces = marching_cubes_to_mesh(mask_bone, spacing)

# 4. Define y ejecuta la simulación en FEBio
sim = FebioSimulation()
sim.add_mesh("hueso", vertices, faces, material="Mooney-Rivlin", properties={...})
sim.run(output_dir="results/")

# 5. Carga y visualiza resultados
show_mesh("results/hueso.vtk", scalar_field="stress")
```



## Contribuir

1. Haz fork del repositorio  
2. Crea una rama nueva (`git checkout -b feature/mi-nueva-funcionalidad`)  
3. Haz tus cambios y añade tests  
4. Abre un Pull Request describiendo tu contribución  

---

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Consulta el fichero [LICENSE](LICENSE) para más detalles.





