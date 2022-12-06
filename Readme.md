#PROJETO FINAL DA DISCIPLINA (AVALIAÇÃO 2)
  
 ALUNO CAIO VINICIUS DE A. Santos ID 1142214088

 Entrada e sáida de dados em formato JSON.Implementados para testes.
  
- /pessoas [GET]: RETORNO a Lista de todas as pessoas</li>
- /pessoa/numerodoTelefone [GET]: RETORNO os dados de uma pessoa pelo Telefone. Exemplo:/pessoa/1140028922
- /pessoa/numerodoTelefone [DELETE]: REMOVER um Telefone existente, tendo retorno removido ou not_found se o Telefone não for encontrado. Exemplo: pessoa/1140028922
- /pessoa [POST]: INSERE ou ATUALIZA uma pessoa com entrada em formato JSON. Se o Telefone mencionado for encontrado, os dados são atualizados. Senão, a nova pessoa é inserida. Exemplo:
    
```
    	{
            "id": "1",
            "nome": "caio", 
            "sobrenome": "Santos",
            "telefone": "1140028922"
            "email": "caaaaio.vini@gmail.com", 
            "idioma": "Portugues"
        }
```
