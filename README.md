# Aplicativo de fotos

Este projeto consiste em um aplicativo de fotos desenvolvido e Python. O sistema tem como foco a ordenação das postagens, usuários, seguidos e seguidores de acordo com alguns critérios. Esses dados são obtidos dos arquivos .bin, onde todas as infoirmações estão inclusas, e a partir disso será gerado um arrquivo .txt com o feed do usuário selecionado.

A versão inicial do aplicativo armazena as informações em um dicionários Python. A chave do dicionário é o login do usuário, e o conteúdo é uma tupla com 4 informações, ficando da seguinte forma: {"login_usuario":"(nome_do_usuario, [usuarios_seguidos], [seguidores], [postagens_feitas]"}.

O algoritmo de ordenação utilizado foi o Merge Sort, e foram feitas modificações para adaptar ele ao nosso código.

## Autores

- [@rafaeldeps](https://www.github.com/rafaeldeps)
- [@ronnaldw](https://www.github.com/ronnaldw)
