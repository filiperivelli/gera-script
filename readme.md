## Documenta��o do Script de Gera��o de Comandos INSERT

### Instala��o

1. Certifique-se de ter o Python instalado. Se necess�rio, voc� pode baix�-lo e instal�-lo a partir do [site oficial do Python](https://www.python.org/).

2. Instale a biblioteca pandas, que � usada para processar dados do Excel. Voc� pode instalar a biblioteca usando o pip, executando o seguinte comando no terminal ou prompt de comando:

    ```
    pip install pandas
    ```

### Funcionamento

1. Baixe o script Python fornecido e salve-o em um local conveniente.

2. Certifique-se de ter um arquivo Excel pronto contendo os dados que voc� deseja processar. Certifique-se de que a segunda linha contenha os nomes das colunas.

3. Abra um terminal ou prompt de comando e navegue at� o diret�rio onde voc� salvou o script Python e o arquivo Excel.

4. Execute o script Python, fornecendo o nome do arquivo Excel como argumento. Por exemplo:

    ```
    python script.py arquivo.xlsx
    ```

    Substitua `script.py` pelo nome do script Python e `arquivo.xlsx` pelo nome do seu arquivo Excel.

5. O script ler� o arquivo Excel, gerar� comandos `INSERT` para cada linha de dados, e imprimir� os comandos na sa�da padr�o. Certifique-se de que a sa�da esteja sendo redirecionada para um arquivo ou visualize os comandos conforme necess�rio.

6. Os comandos `INSERT` gerados podem ent�o ser utilizados para inserir os dados em um banco de dados, conforme apropriado.

### Observa��es

- Certifique-se de que o arquivo Excel est� no mesmo formato esperado pelo script (ou seja, a segunda linha cont�m os nomes das colunas).
- Este script assume que todos os valores no arquivo Excel s�o strings e os formata como tal nos comandos `INSERT`. Certifique-se de ajustar conforme necess�rio de acordo com o tipo de dados em suas colunas.
- O script pode ser modificado e ajustado conforme necess�rio para atender a requisitos espec�ficos do projeto.
