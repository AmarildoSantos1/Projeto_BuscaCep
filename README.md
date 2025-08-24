# Projeto Consulta CEP

Este é um projeto simples em Python desenvolvido para demonstrar os conceitos fundamentais de Integração Contínua (CI) com GitLab CI.

O módulo principal permite consultar endereços brasileiros a partir de um CEP, utilizando a API pública e gratuita [ViaCEP](https://viacep.com.br/).

## Funcionalidades

- `buscar_endereco(cep)`:  
  Recebe um CEP (string de 8 dígitos) e retorna um dicionário com os dados do endereço correspondente.

## Pipeline de Integração Contínua (CI)

Este projeto está configurado com um pipeline de CI básico que é acionado a cada `git push`. O pipeline garante que o código novo seja testado automaticamente antes de ser integrado.

O pipeline é definido no arquivo `.gitlab-ci.yml` e possui os seguintes estágios:

### build

- **Job:** `instalar_dependencias`  
- **Descrição:**  
  Prepara o ambiente e instala todas as dependências do projeto

### test

- **Job:** `executar_testes`  
- **Descrição:**  
  Executa a suíte de testes unitários com o `pytest`. Os testes utilizam a biblioteca `pytest-mock` para simular as respostas da API externa, garantindo que o pipeline seja rápido e não dependa da disponibilidade do serviço ViaCEP. Nesse caso,antes de executar os testes, as dependências listadas no arquivo `requirements.txt` são instaladas na etapa de build.

---

O objetivo deste pipeline inicial é validar que as funcionalidades existentes continuam a funcionar corretamente após cada alteração no código.
