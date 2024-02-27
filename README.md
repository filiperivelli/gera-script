## Documentação do Script de Geração de Comandos INSERT

### Instalação

1. Certifique-se de ter o Python instalado. Se necessário, você pode baixá-lo e instalá-lo a partir do [site oficial do Python](https://www.python.org/).

2. Instale a biblioteca pandas, que é usada para processar dados do Excel. Você pode instalar a biblioteca usando o pip, executando o seguinte comando no terminal ou prompt de comando:

    ```
    pip install pandas
    ```
3. Instale a biblioteca openpyxl, que também é usada para processar dados do Excel. Você pode instalar a biblioteca usando o pip, executando o seguinte comando no terminal ou prompt de comando:
   ```
   pip install openpyxl
   ```

### Funcionamento

1. Baixe o script Python fornecido e salve-o em um local conveniente.

2. Certifique-se de ter um arquivo Excel pronto contendo os dados que você deseja processar. Certifique-se de que a segunda linha contenha os nomes das colunas.

3. Abra um terminal ou prompt de comando e navegue até o diretório onde você salvou o script Python e o arquivo Excel.

4. Execute o script Python, fornecendo o nome do arquivo Excel como argumento. Por exemplo:

    ```
    python script.py arquivo.xlsx
    ```

    Substitua `script.py` pelo nome do script Python e `arquivo.xlsx` pelo nome do seu arquivo Excel.

5. O script lerá o arquivo Excel, gerará comandos `INSERT` para cada linha de dados, e imprimirá os comandos na saída padrão. Certifique-se de que a saída esteja sendo redirecionada para um arquivo ou visualize os comandos conforme necessário.

6. Os comandos `INSERT` gerados podem então ser utilizados para inserir os dados em um banco de dados, conforme apropriado.

### Observações

- Certifique-se de que o arquivo Excel está no mesmo formato esperado pelo script (ou seja, a segunda linha contém os nomes das colunas).
- Este script assume que todos os valores no arquivo Excel são strings e os formata como tal nos comandos `INSERT`. Certifique-se de ajustar conforme necessário de acordo com o tipo de dados em suas colunas.
- O script pode ser modificado e ajustado conforme necessário para atender a requisitos específicos do projeto.

