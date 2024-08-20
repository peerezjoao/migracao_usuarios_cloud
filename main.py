# importa as bibliotecas necessárias
import boto3 
from botocore.exceptions import ClientError
import os 
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

# captura o arquivo .xslx --> será considerado a base de dados desse script
file = os.path.join(os.getcwd(), "users.xlsx")
print(file)

# realizar a leitura da base de dados
dt_users = pd.read_excel(file, sheet_name='Sheet1')
print(dt_users.head())
dt5 = dt_users[:1]

# cria uma sessão com o boto3 --> sdk da aws
session = boto3.Session(
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY"),
)
iam_client = session.client("iam")

for index, row in dt5.iterrows():

    print(row)
    try:
        # cria um novo usuário na aws
        response_create_user = iam_client.create_user(
            UserName = row["users"],
        )
        # cria uma senha para um usuário especifico
        response_create_login = iam_client.create_login_profile(
            UserName = row["users"],
            Password = row["password"], 
            PasswordResetRequired = True
        )
        # adiciona um usuário a um grupo especifico 
        response_add_group = iam_client.add_user_to_group(
            GroupName = row["groups"],
            UserName = row["users"]
        )
    # retorna o erro
    except ClientError as e:
        print(f"Fail to create user. Exception - {e}")
