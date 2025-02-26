# TPC1

- 26/02/2025
- Miguel Gramoso, a100835

## Resumo

Criar um programa que receba um ficheiro _markdown_ e converta os elementos textuais para HTML.

## Procedimento
- **Headers**: in: `## Exemplo`; out: `<h2>Exemplo</h2>`
- **Bold**: in: `**Exemplo**`; out: `<b>Exemplo</b>`
- **Itálico**: in: `*Exemplo*`; out: `<i>Exemplo</i>`
- **Lista Numerada**: 
    in:
    ```
        1. Item1
        2. Item2
        3. Item3
    ```
    out:
    ```html
        <ol>
            <li>Item1</li>
            <li>Item2</li>
            <li>Item3</li>
        </ol>
    ```
- **Link**: in: `Como pode ser consultado em [página da UC](http://www.uc.pt)`; out: `Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>`
- **Imagem**: in: `Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ...`; out: ` Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem
dum coelho"/> ...`

## Resultados

Utilizando o comando `python3 tpc3.py < example.txt`, obtém-se:
```
<h1>Exemplo</h1>

Este é um <b>exemplo</b> ...

Este é um <i>exemplo</i> ...

<ol>
<li>Primeiro item</li>
<li>Segundo item</li>
<li>Terceiro item</li>
</ol>
Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>

Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/>
```