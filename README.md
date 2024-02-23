# Título 1

## Título 2

### Título 3

**Texto em negrito**

*Texto em itálico*

- Item 1
- Item 2
  - Subitem 2.1
  - Subitem 2.2

1. Primeiro item
2. Segundo item
3. Terceiro item


[Texto do link](URL)

![Texto alternativo da imagem](https://avatars.githubusercontent.com/u/155449465?s=400&u=6ff98dcf9214b5398b2dd1dcba889a1681a36cc1&v=4)

### Citações


### Linhas horizontais


`Código em linha`

```python
# Bloco de código em Python
print("Olá, mundo!")

```


Essas são apenas algumas das formatações básicas disponíveis em Markdown. Existem muitas outras opções e variações, mas essas são as mais comuns.

# Remover bibliotecas python
pip freeze | grep -v "^-e" | xargs pip uninstall -y