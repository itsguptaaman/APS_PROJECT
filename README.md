### **APS Project**


### Step 1 - Install the requirements

```bash
pip install -r requirements.txt
```

### Step 2 - Run main.py file

```bash
python main.py
```

### To download the dataset 
```
wget https://raw.githubusercontent.com/itsguptaaman/APS_PROJECT/main/aps_failure_training_set1.csv
```

### To check and reset git log
```
git log
git reset --soft 6afd
6afd -> last 4 digit of log. 
```

### To add and uplod to git
```
git add filename
we can also use . for all file(Current directory)

git commit -m "Message"
git push origin main
```

### To run jupyter-notebook in vscode
```
 pip install ipykernel
```

### **To create a new environment in vscode** 
```
 1. Select the command prompt as a terminal 
conda create -p venv python==3.7 -y
```

### Create a .env It contains details.
```
MONGO_DB_URL="mongodb://localhost:27017/neurolabDB"
AWS_ACCESS_KEY_ID="aagswdiquyawvdiu"
AWS_SECRET_ACCESS_KEY="sadoiuabnswodihabosdbn"
```

```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

```
AWS_ACCESS_KEY_ID =
AWS_SECRET_ACCESS_KEY =
AWS_REGION =
AWS_ECR_LOGIN_URI =
ECR_REPOSITORY_NAME =
BUCKET_NAME =
MONGO_DB_URL =
```