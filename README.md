# 🇧🇷 CPF Validator: Validador de Documento em Python

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Status](https://img.shields.io/badge/Status-Funcional-brightgreen.svg)]()

Este script Python implementa o algoritmo de validação de **Cadastro de Pessoas Físicas (CPF)**, que é o documento de identificação fiscal padrão no Brasil.

O código faz a leitura sequencial dos 11 dígitos fornecidos pelo usuário e recalcula os dois dígitos verificadores (DVs) utilizando a lógica do **Módulo 11 (Mod 11)**. Em seguida, compara os dígitos calculados com os dígitos fornecidos pelo usuário para determinar a validade do CPF.

## ✨ Características e Lógica

* **Cálculo Mod 11:** Implementação da lógica padrão para calcular o 1º (décimo) e 2º (décimo primeiro) dígitos verificadores.
* **Validação em Loop:** Permite a entrada e validação contínua de múltiplos CPFs até que o usuário decida parar.
* **Coleta de Entrada:** Garante que o usuário insira apenas números positivos de 0 a 9.
* **Relatório Final:** Gera um resumo estatístico simples ao final da execução (total de CPFs, válidos, inválidos e porcentagens).

---

## 🚀 Guia de Início Rápido

### Pré-requisitos
Certifique-se de ter o **Python (3.6 ou superior)** instalado.

### 1. Clonagem e Execução
Clone o repositório (usando seu usuário `bizogue`) e execute o script diretamente:

```bash
git clone [https://github.com/bizogue/cpf-validator-python.git](https://github.com/bizogue/cpf-validator-python.git)
cd cpf-validator-python
python cpf_validator.py
