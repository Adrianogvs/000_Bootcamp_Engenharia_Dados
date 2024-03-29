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


## Primeiro passo a ser realizado é instalar o pyenv, no caso de SO Windows, usa o link abaixo:

https://github.com/pyenv-win/pyenv-win

Logo após abre o PowerShell e colar esse código:

```
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
```

![!\[alt text\](image.png)](pic/powershell.png)

Logo após verificar se o pyenv foi instado na maquina, basta acessar o bash e digitar o seguinte código:

```
$ pyenv --version
```
![alt text](pic/pyenv.png)


## Remover bibliotecas python
`pip freeze | grep -v "^-e" | xargs pip uninstall -y`

## Remover todas as versões do pyenv

```
$ #!/bin/bash

versions=$(pyenv versions --bare)

for version in $versions
do
    if [[ $version != "*" ]]; then
        echo "Removendo a versão $version..."
        pyenv uninstall $version
    fi
done
```


## Erro durante a instalação do ipython

Adriano@agvs-001 MINGW64 ~/Documents/GitHub/000_Bootcamp_Engenharia_Dados (main)
```
$ pipx install ipython --force`
```
```
creating virtual environment...
installing ipython...
Note: 'C:\Users\Adriano\.local\bin' is not on your PATH environment
    variable. These apps will not be globally accessible until your PATH is
    updated. Run `pipx ensurepath` to automatically add it, or manually modify
    your PATH in your shell's config file (i.e. ~/.bashrc).
done!
Installing to existing venv 'ipython'
  installed package ipython 8.22.1, installed using Python 3.12.1
  These apps are now globally available
    - ipython.exe
    - ipython3.exe
  These manual pages are now globally available
    - man1\ipython.1
    ´
```

'Adriano@agvs-001 MINGW64 ~/Documents/GitHub/000_Bootcamp_Engenharia_Dados (main)
```
$ ipython -i
```

```
bash: ipython: command not found
```
Adriano@agvs-001 MINGW64 ~/Documents/GitHub/000_Bootcamp_Engenharia_Dados (main)
```
$ export PATH="$PATH:/c/Users/Adriano/.local/bin"
```
Adriano@agvs-001 MINGW64 ~/Documents/GitHub/000_Bootcamp_Engenharia_Dados (main)
```
$ ipython -i`
```
Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.22.1 -- An enhanced Interactive Python. Type '?' for help.
```
In [1]:
```


## Recriando pasta django com poetry
Adriano@agvs-001 MINGW64 ~/Documents/GitHub/000_Bootcamp_Engenharia_Dados (main)

```
$ poetry config virtualenvs.in-project true
```


Adriano@agvs-001 MINGW64 ~/Documents/GitHub/000_Bootcamp_Engenharia_Dados (main)

```
$ poetry new projeto_django
```
Created package projeto_django in projeto_django
```

Adriano@agvs-001 MINGW64 ~/Documents/GitHub/000_Bootcamp_Engenharia_Dados (main)

`$ cd projeto_django/`

Adriano@agvs-001 MINGW64 ~/Documents/GitHub/000_Bootcamp_Engenharia_Dados/projeto_django (main)

`
$ poetry env use 3.12.1
`
```
Creating virtualenv projeto-django in C:\Users\Adriano\Documents\GitHub\000_Bootcamp_Engenharia_Dados\projeto_django\.venv
Using virtualenv: C:\Users\Adriano\Documents\GitHub\000_Bootcamp_Engenharia_Dados\projeto_django\.venv
```
Adriano@agvs-001 MINGW64 ~/Documents/GitHub/000_Bootcamp_Engenharia_Dados/projeto_django (main)
```
```
$ poetry add django
