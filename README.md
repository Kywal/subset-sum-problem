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
3. Será exibido um menu com 8 opções, sendo as 4 primeiras para escolher executar entre um dos algoritmos e as 4 últimas referentes as ao gerador de instâncias, instruções e interação com o menu:
    ```bash
   +------------------------------+
   |           MENU               |
   +------------------------------+
   (0) Digite 0 para executar o EXATO FFT numa instância que já se encontra na pasta.
   (1) Digite 1 para executar o EXATO SIMPLES numa instância que já se encontra na pasta.
   (2) Digite 2 para executar o APROXIMATIVO numa instância que já se encontra na pasta.
   (7) Digite 7 para executar o EXATO MP numa instância que já se encontra na pasta.
   (3) Para instruções sobre instâncias específicas.
   (4) Para gerar uma nova instância aleatória digite 4.
   (5) Para encerrar digite 5.
   (6) Exibir o menu novamente.
    ```

4. Digitando 0, 1, 2 ou 7 será possível executar um dos algoritmos em uma instância que já está na pasta *datatest*. Para isso será solicitado informar o nome da instância, isto é, o nome do arquivo sem extensão, como no exemplo abaixo no qual foi escolhida a instância *p01*.
   ```bash
   Informe o nome da instância que deseja executar (ex.: p01, p02...):p01
   ```
5. O resultado será exibido em tela e também salvo em um relatório com mesmo nome do arquivo em uma das pastas correspondentes *reports_aprox*, *reports_exact_fft*, *reports_exact_mp* e *reports_exact_simple*.
   
6. Digitando 4 no menu será possível gerar uma instância aleatória para teste e em seguida executar o algoritmo nela. Note que o nome do arquivo criado para a instância é exibido na penúltima linha e pode ser utilizado como entrada na solicitação seguinte.
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
