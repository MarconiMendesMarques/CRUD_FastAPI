
# fastAPI_CRUD 

API destinada a criação, leitura, alteração e deleção
em cadastro de usuários PostgreSql utilizando Python, fastAPI e Ormar.


## Referências

 - [FastAPI](https://fastapi.tiangolo.com)
 - [ORMAR](https://collerek.github.io/ormar/)
 - [PostgreSQL](https://www.postgresql.org/)


## Documentação da API

#### Retorna todos os usuários

```http
  GET/usuarios/
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
|      -      |      -     |          -                           |

#### Adiciona um usuário - CREATE

```http
  POST/usuarios/
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
|    `-`      |      `-`   |        - |


#### Retorna um usuário - READ

```http
  GET/usuarios/{usuario_id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `  id`      | `string`   |  **Obrigatório**. O ID do usuario que você quer |

#### Edita um usuário - UPDATE

```http
  PUT/usuarios/{usuario_id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `  id`      | `string`   |  **Obrigatório**. O ID do usuario que você quer |


#### Deleta um usuário - DELETE

```http
  DELETE/usuarios/{usuario_id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `  id`      | `string`   |  **Obrigatório**. O ID do usuario que você quer |




## Rodando localmente


- Download do arquivo fastAPICodhab.zip
- Descompactar na pasta desejada
- Criar ambiente virtual:  

        python -m venv <nome_do_ambiente>
- Ativar ambiente criado:
  
        source <nome_do_ambiente>/bin/activate 
- Verificar dependências e apps instalados. Não deve haver nada
  
        pip freeze 
- Instalar dependências/apps:
  
        pip install -r requirements.txt 
- Configurar arquivo config.config.py 
- Configurar o arquivo cria_tabelas


- Rodar o servidor uvicorn (localhost):
        
        uvicorn main:app 
    
- No browser: 

        http://127.0.0.1:8000/docs