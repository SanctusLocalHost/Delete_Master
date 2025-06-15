# Delete Master - Cyberpunk Edition (V1.4)

**ATENÇÃO: ESTE PROGRAMA APAGA ARQUIVOS! USE COM EXTREMO CUIDADO E APENAS SE SOUBER EXATAMENTE O QUE ESTÁ FAZENDO. O USO INDEVIDO PODE LEVAR À PERDA IRREVERSÍVEL DE DADOS, INCLUINDO ARQUIVOS DO SISTEMA.**

## Descrição

O **Delete Master** é uma ferramenta com interface gráfica (GUI) projetada para deletar arquivos em diretórios específicos com base em critérios definidos pelo usuário. Ele possui um tema escuro "Cyberpunk Neon" para uma experiência visual diferenciada.

## Preview
Aviso Inicial
![image](https://github.com/user-attachments/assets/620bea1c-f749-4e17-8b8e-b685f418b32a)

Programa Iniciado
![image](https://github.com/user-attachments/assets/7e691dcd-5fcb-4186-bc73-aff6c308e2c2)

## Funcionalidades

*   **Seleção de Diretório:** Escolha a pasta onde a exclusão de arquivos será realizada.
*   **Intervalo de Datas:** Defina uma data inicial e final para filtrar arquivos pela data de modificação.
*   **Seleção de Formatos:** Marque os tipos de arquivo que deseja excluir (ex: `.xlsx`, `.pdf`, `.zip`, etc.).
*   **Palavra de Exceção:** Insira uma palavra-chave (opcional). Arquivos que contiverem essa palavra no nome não serão deletados.
*   **Pop-up de Aviso:** Um aviso é exibido ao iniciar o programa, reforçando a natureza destrutiva da ferramenta.
*   **Barra de Progresso:** Acompanhe o processo de análise e exclusão de arquivos em tempo real.
*   **Interface Cyberpunk:** Tema escuro com cores neon.

## Requisitos

Para executar este programa, você precisará ter o Python instalado, juntamente com as seguintes bibliotecas:

*   `customtkinter`
*   `tkcalendar`
*   `Pillow` (opcional, mas incluída para compatibilidade futura com imagens)

## Como Usar

1.  **Instale as dependências:**
    ```bash
    pip install customtkinter tkcalendar Pillow
    ```

2.  **Execute o script:**
    Salve o código como um arquivo Python (por exemplo, `delete_master.pyw` ou `delete_master.py`) e execute-o:
    ```bash
    python delete_master.pyw
    ```
    ou
    ```bash
    python delete_master.py
    ```

3.  **Confirme o Aviso:** Leia atentamente o pop-up de aviso e clique em "ESTOU CIENTE E QUERO PROSSEGUIR" se concordar.

4.  **Configure os Filtros:**
    *   Clique em "Procurar" para selecionar o diretório alvo.
    *   Defina o intervalo de datas.
    *   Marque os formatos de arquivo a serem deletados.
    *   Opcionalmente, adicione uma palavra de exceção.

5.  **Delete os Arquivos:**
    *   Clique no botão "DELETAR ARQUIVOS SELECIONADOS".
    *   Uma segunda confirmação será solicitada, mostrando o número de arquivos a serem deletados.
    *   Se confirmar, os arquivos serão excluídos permanentemente.

## Importante

*   **Faça backups:** Antes de usar esta ferramenta em diretórios importantes, certifique-se de ter backups dos seus dados.
*   **Verifique os caminhos:** Confirme duas vezes o diretório selecionado antes de prosseguir com a exclusão.
*   **A exclusão é irreversível.**

---

Use por sua conta e risco.
