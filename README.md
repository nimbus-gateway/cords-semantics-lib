# Cords-Semantics

Cords-Semantics is a Python library designed for tagging the artifacts of MLflow runs and generating semantic descriptions for artifacts using the ontology provided by CORDS. This library helps interpret and utilize data from MLflow runs more effectively in machine learning projects, and prepares the assets to be shared in an IDSA (International Data Spaces Association) ecosystem.


## Features

- **Tagging Artifacts**: Automatically tag MLflow run artifacts with relevant semantic information.
- **Semantic Descriptions**: Generate semantic descriptions for MLflow artifacts using CORDS ontology.
- **Data Interpretation**: Enhance the interpretability of MLflow run data.
- **Integration with IDSA**: Prepare and format data for sharing within an IDSA-compliant ecosystem.


## Build Project

This project uses Poetry for dependency management. To get started, you'll need to install Poetry if you haven't already:

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

# Use poetry to build the project. Build files are in dist folder
poetry build


# Installation
