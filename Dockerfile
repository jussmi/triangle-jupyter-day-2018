FROM jupyter/minimal-notebook

USER $NB_UID

RUN python -m pip install tqdm

