<h1 align="center">LINKER-Pred2</h1>
<p align="center"><i>A Disordered Flexible Linker (DFL) ppredictor trained on DLD domain Linker dataset and <a href="https://disprot.org/">Disprot</a> Database.</i></p>

## 📝 Description
LINKER-Pred2 project belongs to a series of LINKER-Pred-Suite projects which focus on the Structure and Function prediction of Disordered Flexible Linkers (DFLs).
Currently we have <a href="https://github.com/deemeng/punch_linker_light">LINKER-Pred2</a> for fast DFL prediction and <a href="https://github.com/deemeng/punch_linker2">LINKER-Pred2</a> for more accurate DFL prediction.
LINKER-Pred2 is trained on more than 2000 DFL linker dataset from our <a href="https://pcrgwd.ucd.ie/linker">DLD</a> dataset and <a href="https://disprot.org/">Disprot</a>, its performance is better than TOP predictors on the CAID2 Linker dataset.

## 🐣 Getting Started
Currently, we provide two ways to use this predictor: Docker or download the source code from GitHub.
### Pre-requirements
This predictor requires sequences embedded with [ProtTrans](https://github.com/agemagician/ProtTrans) and [MSA Transformer](https://github.com/facebookresearch/esm).
Note, 
* File format should be `[SEQUENCE_NAME/ID].npy`, replace *SEQUENCE_NAME/ID* with the actual sequence ID, it should be the same as the name from the `.fasta` file.
* Matrix shape: \
  **Onehot**: `(1, SEQUENCE_LENGTH, 21)` \
  **ProtTrans**: `(1, SEQUENCE_LENGTH, 1024)` \
  **MSA Transformer**: `(1, SEQUENCE_LENGTH, 768)`

📣‼️If you don't have them available, please visit the **[embedding](https://github.com/deemeng/embedding)** section of our project first to embed the sequences.‼️

(We maintain this separation due to the requirements from [CAID3](https://caid.idpcentral.org/challenge), but we may edit or merge them in the future.)
### Docker (Recommended)
#### Dependencies
* Go to **[embedding](https://github.com/deemeng/embedding)** if you don't have [ProtTrans](https://github.com/agemagician/ProtTrans) and [MSA Transformer](https://github.com/facebookresearch/esm) embedded sequences;
* Docker Desktop 4.27.2 or higher;
#### Installing
* Pull the Docker image from  <a href="https://hub.docker.com/repository/docker/dimeng851/punch_linker2/tags">DockerHub</a>
  ```sh
  docker pull dimeng851/punch_linker2:v2
  ```

#### Executing program
* RUN the following command:
  >Replace \
  >`CONTAINER_NAME` - any name you like; \
  >`PATH_TO_INPUT_FASTA` - path to input file, which is **ONE** FASTA file including all query sequences; \
  >`PATH_TO_MSATRANS` - a folder which includes all MSA Transformer embedded sequences; \
  >`PATH_TO_PROTTRANS` - a folder which includes all protTrans embedded sequences; \
  >`PATH_OUTPUT` - a folder which will be used to save all outputs, including: a. timings.csv; b. disorder folder, where will keep all the prediction resulds.
  ```sh
  docker run -d \
  -it \
  --name [CONTAINER_NAME] \
  --mount type=bind,source=[PATH_TO_INPUT_FASTA],target=/punch_linker2/data/input.fasta \
  --mount type=bind,source=[PATH_TO_MSATRANS],target=/punch_linker2/data/msaTrans \
  --mount type=bind,source=[PATH_TO_PROTTRANS],target=/punch_linker2/data/protTrans \
  --mount type=bind,source=[PATH_OUTPUT],target=/punch_linker2/output \
  dimeng851/punch_linker2:v2
  ```
  > 
  >An example:
  ```sh
  docker run -d \
  -it \
  --name punch_linker2_con \
  --mount type=bind,source=/Users/deemeng/Downloads/data/linker/linker.fasta,target=/punch_linker2/data/input.fasta \
  --mount type=bind,source=/Users/deemeng/Downloads/data/linker/msaTrans,target=/punch_linker2/data/msaTrans \
  --mount type=bind,source=/Users/deemeng/Downloads/data/linker/protTrans,target=/punch_linker2/data/protTrans \
  --mount type=bind,source=/Users/deemeng/Downloads/data/linker/output,target=/punch_linker2/output \
  dimeng851/punch_linker2:v2
  ```
* Find the results in **OUTPUT** folder.

## Contact & Help 📩

Email Di.
```
di.meng@ucdconnect.ie
```

## Authors
📬 Di Meng - di.meng@ucdconnect.ie \
📬 Juliana Glavina - jglavina@iib.unsam.edu.ar \
📬 Gianluca Pollastri - gianluca.pollastri@ucd.ie \
📬 Lucía Beatriz Chemes - lchemes@iib.unsam.edu.ar 

## Project
>https://github.com/deemeng/punch_linker2
