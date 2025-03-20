 TPC4

![Nome do Autor](../profile.jpg)  
- 02/03/2025
- Miguel Gramoso, a100835

## Resumo

Criar um analisador léxico capaz de detetar e _tokenizar_ a linguagem de _query_ proposta:


## Procedimento

1. Verificar e especificar os _tokens_ a serem tratados.
2. Criar expressões regulares para obter grupos de captura.
3. Para casos mais específicos, acrescentar regras extra.

## Resultados

Utilizando o comando `python3 tpc4.py < example.txt`, obtém-se o seguinte resultado:

```
[('select', 'KEYWORD'), ('?nome', 'VAR'), ('?desc', 'VAR'), ('where', 'KEYWORD'), ('{', 'SYMBOL'), ('?s', 'VAR'), ('dbo:MusicalArtist', 'URI'), ('.', 'SYMBOL'), ('?s', 'VAR'), ('foaf:name', 'URI'), ('"Chuck Berry"@en', 'STRING'), ('.', 'SYMBOL'), ('?w', 'VAR'), ('dbo:artist', 'URI'), ('?s', 'VAR'), ('.', 'SYMBOL'), ('?w', 'VAR'), ('foaf:name', 'URI'), ('?nome', 'VAR'), ('.', 'SYMBOL'), ('?w', 'VAR'), ('dbo:abstract', 'URI'), ('?desc', 'VAR'), ('}', 'SYMBOL'), ('1000', 'NUMBER')]
```