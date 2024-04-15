<h1 align="center">LINKER-Pred2</h1>
<p align="center"><i>A Disordered Flexible Linker (DFL) ppredictor trained on DLD domain Linker dataset and <a href="https://disprot.org/">Disprot</a> Database.</i></p>

## 📝 Description
LINKER-Pred2 project belongs to a serious of PUNCH projects which focus on the Structure and Function prediction of Intrisically Diordered Protein/Region (IDP/IDR).
Currently we have <a href="https://github.com/deemeng/punch2">PUNCH2</a> for IDR structure prediction and <a href="https://github.com/deemeng/punch_linker2">LINKER-Pred</a> for DFL prediction.
PUNCH_Linker is trained on more than 2000 DFL linker dataset from <a href="https://disprot.org/">DLD</a> dataset and <a href="https://disprot.org/">Disprot</a>, its performance is better than TOP predictors on the CAID2 Linker dataset.

## 🐣 Getting Started
### Pre-requirements
This predictor requires sequences embedded with [ProtTrans](https://github.com/agemagician/ProtTrans) and [MSA Transformer](https://github.com/facebookresearch/esm).
Note, 
* File format should be `[SEQUENCE_NAME/ID].npy`, replace *SEQUENCE_NAME/ID* with the actural sequence ID, it should be the same as the name from `.fasta` file.
* Matrix shape: \
  **ProtTrans**: `(1, SEQUENCE_LENGTH, 1024)` \
  **MSA Transformer**: `(1, SEQUENCE_LENGTH, 768)`

📣‼️If you don't have them available, please visit the **[embedding](https://github.com/deemeng/embedding)** section of our project first to embed the sequences.‼️

(We maintain this separation due to the requirements from [CAID3](https://caid.idpcentral.org/challenge), but we may edit or merge them in the future.)
### Docker (Recommend)
#### Dependencies
* Go to **[embedding](https://github.com/deemeng/embedding)** if you don't have [ProtTrans](https://github.com/agemagician/ProtTrans) and [MSA Transformer](https://github.com/facebookresearch/esm) embedded sequences;
* Docker Desktop 4.27.2 or higher;
#### Installing
* Pull the Docker image from  <a href="https://hub.docker.com/repository/docker/dimeng851/punch_linker/tags">DockerHub</a>
  ```sh
  docker pull dimeng851/punch_linker2:v1
  ```

#### Executing program
* RUN the following command:
  >Replace \
  >`CONTAINER_NAME` - anyname you like; \
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
  dimeng851/punch_linker2:v1
  ```
  > 
  >An example:
  ```sh
  docker run -d \
  -it \
  --name punch_linker2_con \
  --mount type=bind,source=/home/dimeng/caid3/test.fasta,target=/punch_linker2/data/input.fasta \
  --mount type=bind,source=/home/dimeng/project/domain_linker/data/caid/features/msaTrans,target=/punch_linker2/data/msaTrans \
  --mount type=bind,source=/home/dimeng/project/domain_linker/data/caid/features/protTrans,target=/punch_linker2/data/protTrans \
  --mount type=bind,source=/home/dimeng/caid3/punch_linker_output,target=/punch_linker2/output \
  dimeng851/punch_linker2:v1
  ```
* Find the results in **OUTPUT** folder.

## Contact & Help 📩

Email Di.
```
di.meng@ucdconnect.ie
```

## Authors
📬 Di Meng - di.meng@ucdconnect.ie \
📬 Gianluca Pollastri - gianluca.pollastri@ucd.ie 

## Project
>https://github.com/deemeng/punch_linker2
