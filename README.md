# Cords-Semantics

Cords-Semantics is a Python library designed for tagging the artifacts of MLflow runs and generating semantic descriptions for artifacts using the ontology provided by CORDS. This library helps interpret and utilize data from MLflow runs more effectively in machine learning projects, and prepares the assets to be shared in an IDSA (International Data Spaces Association) ecosystem.


## Features

- **Tagging Artifacts**: Provide the CORDS vocab in as a set of MLFlow tags to be used during the training.
- **MLFlow MetaData Extractions**: Provide interfaces to extract MLflow tags and other metadata to a JSON structure 
- **Generate Semantic Description**: Automatically generate semantic descriptions for MLflow artifacts.



## Build Project

This project uses Poetry for dependency management. To get started, you'll need to install Poetry if you haven't already:

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

# Use poetry to build the project. Build files are in dist folder
poetry build
```

## Installation

Install from the built filename.gz from the dist folder
```bash
cd dist
pip install cords_semantics-0.1.0.tar.gz
```

