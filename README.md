# Typing Test

![Versão](https://img.shields.io/badge/vers%C3%A3o-0.4.0-brightgreen)
![Licença](https://img.shields.io/badge/licen%C3%A7a-Unlicense-blue)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

Um software de digitação desenvolvido para treinar a velocidade e a precisão dos usuários. Ele oferece estatísticas em tempo real.

### O executável compilado na última versão se encontra em: https://drive.google.com/drive/folders/1dPQk-8pNkK6yiJjFtP6Rgawihpi4RsA9?usp=sharing

## Recursos Principais

- **Estatísticas em Tempo Real**: Acompanhe palavras por minuto(WPM) e precisão.
- **Modos de Treinamento**:
  - Testes Cronometrados

---
## Instalação

### Pré-requisitos
- **Python+3.10**
- **Poetry**
- **Git**

### Passos para Instalação

**1. Clone o repositório para sua máquina local:**

  ```bash
  git clone https://github.com/Gustavo0121/typing-test.git
  ```

**2. Navegue até o diretório do projeto:**

  ```bash
  cd typing-test
  ```

**3. Instale as dependências:**

  ```bash
  poetry install
  ```

### Como compilar

  ```bash
  flet pack -n typing-test --product-version $(poetry version -s) application/main.py
  ```
---


## Contato
Desenvolvido por [Gustavo Ribeiro](https://github.com/Gustavo0121).
Se tiver dúvidas ou sugestões, entre em contato:
- E-mail: gus0512san@gmail.com
- Github: Gustavo0121