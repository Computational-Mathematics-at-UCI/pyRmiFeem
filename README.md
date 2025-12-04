# PyRMIFEEM

**pyrmifeem** es un Python toolkit para construir y visualizar modelos por Elementos Finitos (FEM) de tejido y estructuras óseas a partir de imágenes de Resonancia Magnética (RMI) almacenadas en ficheros DICOM. Se apoya en pydicom, pyvista y FEBio vía el binding `febio-python` y en librerías de preprocesado, segmentación, mallado y visualización.

---

## Características

- Lectura y preprocesado de volúmenes DICOM
- Segmentación semiautomática de hueso y tejidos blandos  
- Generación de mallas 3D a partir de máscaras segmentadas  
- Simulación FEM con FEBio (hiperelástico, poroelástico, viscoelástico)  
- Visualización interactiva de mallas y resultados con PyVista  

---

## Requisitos previos

1. Anaconda 3 instalado  
2. FEBio 3.x instalado y accesible en tu sistema  
   - Define la variable de entorno `FEBIO_HOME` apuntando al directorio de FEBio  

---

## Instalación

1. Clona este repositorio  

   ```bash
   git clone https://github.com/tu-usuario/pyrmifeem.git
   cd pyrmifeem
   ```

2. Crea un entorno virtual e instala dependencias
**Instalación con Anaconda**

```bash
conda create  -f environment.yml --prefix ./SoftFem
conda activate ./SoftFem
```

---

## Estructura del proyecto

```text
pyrmifeem/
├── environment.yml        # Descripción del entorno de anaconda
├── LICENSE                # MIT License
├── prototypes             # Prototipos de prueba y conceptos
│       
├── pyrmifeem              # Código Fuente instalable | |||  │                          # del toolkit               
│   
├── README.md              # Descripción
└── setup.py               # Instalación del múdulo mediante pip
```

---

## Uso básico

Por definir


## Contribuir

1. Haz fork del repositorio  
2. Crea una rama nueva (`git checkout -b feature/mi-nueva-funcionalidad`)  
3. Haz tus cambios y añade tests  
4. Abre un Pull Request describiendo tu contribución  

---

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Consulta el fichero [LICENSE](LICENSE) para más detalles.