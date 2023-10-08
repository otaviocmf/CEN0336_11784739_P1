#!/bin/bash

# Comando que mostra a pasta/diretório onde você está
echo "Diretório atual:"
pwd

# Comando que gera uma lista com detalhes do conteúdo da sua pasta HOME e redirecione essa lista para o arquivo: lista_HOME.txt
ls -l $HOME > lista_HOME.txt

# Comando que imprima a data atual na tela
echo "Data atual:"
date

