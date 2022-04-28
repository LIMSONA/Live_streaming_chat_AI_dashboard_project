#!/bin/bash

/bin/bash -c "source activate conda && jupyter notebook --ip='0.0.0.0' --port=${JUPYTER_PORT} --allow-root --NotebookApp.token='' --NotebookApp.password=''"