# subset-sum-problem
Implementação de um esquema aproximativo para o problema da soma de subconjuntos.

## Execução

1. Após clonar o repositório, acesse a pasta do projeto:
   
   ```bash
   cd subset-sum-problem
    ```
2. Para iniciar a execução do programa, utilize o seguinte comando:
    ```bash
    python main.py
    ```
3. Será exibido um menu com 5 opções:
    ```bash
    ------------------------ MENU ----------------------------
    (1) Se deseja executar numa instância que já se encontra na pasta digite 1.
    (2) Para gerar uma nova instância aleatória digite 2.
    (3) Para instruções sobre instâncias específicas.
    (4) Para encerrar digite 4
    (0) Exibir o menu novamente.
    ```

4. Digitando 1 será possível executar o algoritmo em uma instância que já está na pasta *datatest*. Para isso será solicitado informar o nome da instância, isto é, o nome do arquivo sem extensão, como no exemplo abaixo no qual foi escolhida a instância *p01*.
   ```bash
   Informe o nome da instância que deseja executar (ex.: p01, p02...):p01
   ```
5. O resultado será exibido em tela e também salvo em um relatório com mesmo nome do arquivo na pasta *reports*.
6. Digitando 2 no menu será possível gerar uma instância aleatória para teste e em seguida executar o algoritmo nela. Note que o nome do arquivo criado para a instância é exibido na penúltima linha e pode ser utilizado como entrada na solicitação seguinte.
   ```bash
   Para criar uma nova instância aleatória será necessário informar
   - Quantidade de elementos do conjunto 
   - Intervalo no qual os números se encontram (início e fim positivos)
    Quantidade de elementos do conjunto: 10
    Início do intervalo de números: 1
    Final do intervalo de números: 50
    Arquivo salvo como: datatest/p46.txt <<
    Informe o nome da instância que deseja executar (ex.: p01, p02...):p46
   ```

7. Para adicionar uma instância específica diferente das já disponíveis e não gerada aleatoriamente, basta adicionar na pasta *datatest* um arquivo .txt com o formato abaixo, onde a primeira linha se refere ao valor alvo, a segunda ao conjunto original e a terceira ao subconjunto de solução ótima. Se não houver uma solução ótima para ser fornecida, basta informar uma lista vazia.
   ```bash
   53
   [15, 22, 14, 26, 32, 9,16, 8]
   [22,14,9,8]
   ```
