# TPC1

- 13/01/2025
- Miguel Gramoso, a100835

## Resumo

Somador on/off:

1. Pretende-se um programa que some todas as sequências de dígitos que encontre num texto
2. Sempre que encontrar a string "Off" em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado
3. Sempre que encontrar a string "On" em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado
4. Sempre que encontra o carater "=", o resultado da soma é colocado na saída
5. No fim, é colocado o valor total na saida

_exemplo_:

```
...45...
...2025-02-07...
...Off...
...789...43...
...on...2...
...5 = ...
```

_resultado_

```
ac = 45
+ 2025
+ 2
+ 7 (=2079)
+ 2
+ 5 -> print 2086
```

## Resultados

Executanto o programa com o texto de exemplo, obtem-se o seguinte resultado.

```bash
$ python3 tpc1.py < sample.txt
156
699
2866
```



## Conclusões

O programa revela-se desnecessariamente complexto, mas fucnional.