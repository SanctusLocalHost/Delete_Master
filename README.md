# Delete Master V1.2

## Descrição

O **Delete Master V1.2** é uma ferramenta criada para deletar arquivos em massa de modo automático. Com uma interface simples e intuitiva, permite selecionar um diretório específico, definir um intervalo de tempo, escolher os formatos de arquivo a serem excluídos, e opcionalmente, configurar uma palavra-chave para exceção, garantindo que determinados arquivos não sejam deletados.

### Funcionalidades Principais:
- **Deleção em Massa**: Escolha um diretório e delete múltiplos arquivos simultaneamente com base no intervalo de tempo e nos formatos de arquivo selecionados.
- **Intervalo de Tempo**: Defina uma data inicial e final para deletar apenas os arquivos modificados dentro deste intervalo.
- **Seleção de Formatos**: O software suporta a exclusão de arquivos de diversos formatos como `.xlsx`, `.pdf`, `.zip`, `.png`, `.py`, `.exe` e muitos outros.
- **Exceção por Palavra-Chave**: Insira um termo para garantir que qualquer arquivo contendo essa palavra no nome seja preservado durante o processo de deleção.

## Requisitos

- **Python 3.x**
- **Bibliotecas Python**:
  - `tkinter` – para a criação da interface gráfica.
  - `tkcalendar` – para o widget de seleção de datas.
  - `Pillow` – (opcional) para suporte a imagens no Tkinter.

### Instalando as Dependências:

`bash`
`pip install tkcalendar Pillow`

`python DeleteMaster.pyw`

### Instruções na Interface:

- Escolha o diretório onde os arquivos serão deletados clicando em Procurar.
- Defina o intervalo de tempo (Data Inicial e Data Final) para determinar os arquivos a serem apagados com base na última modificação.
- Selecione os formatos de arquivo que deseja excluir.
- Opcionalmente, insira uma exceção de palavra-chave para garantir que arquivos com essa palavra no nome não sejam apagados.
- Clique em Deletar Arquivos para iniciar o processo.

