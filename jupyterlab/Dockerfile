FROM  quay.io/jupyter/scipy-notebook:notebook-7.4.0

# Install plugins


# Install lsp


# Install bash backend, go backend

RUN mamba install --yes \
  jupyterlab-fasta jupyterlab-geojson jupyterlab-katex jupyterlab-mathjax2 jupyterlab-vega3 \
  'jupyter-ai[all]' jupyterlab-latex jupyterlab-lsp bash_kernel && \
  mamba clean --all -f -y && \
  fix-permissions "${CONDA_DIR}" && \
  fix-permissions "/home/${NB_USER}"

