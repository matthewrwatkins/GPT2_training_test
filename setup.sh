# install conda
wget https://repo.anaconda.com/miniconda/Miniconda3-py310_22.11.1-1-Linux-x86_64.sh | bash
# clean up
rm Miniconda3*.sh

# create conda environment and open it
conda env create --file environment.yaml

# download dataset
env KAGGLE_USERNAME="inamoratapress"
env KAGGLE_KEY="c1038f5a33fe907c3daa7b0dc3c39eee"

pip install kaggle
kaggle datasets download -d neisse/scrapped-lyrics-from-6-genres

