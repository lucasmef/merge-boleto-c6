# PDF Merger - Ordenado por Data de Vencimento 📄

Este script em Python automatiza a tarefa de mesclar múltiplos arquivos PDF em um único documento (`documento_final.pdf`).

O diferencial deste script é a sua capacidade de **ordenar as páginas cronologicamente**, baseando-se em uma data de vencimento extraída diretamente do nome do arquivo.

## 🚀 Funcionalidades

* Busca automática de todos os arquivos `.pdf` no diretório atual.
* Extração inteligente de datas no nome do arquivo (padrão `_venc_DD-MM-AA`).
* Ordenação cronológica dos arquivos antes da mesclagem.
* Tratamento de erros caso a biblioteca necessária não esteja instalada.
* Geração de log no console mostrando a ordem final dos arquivos.

## 📋 Pré-requisitos

Para executar este script, você precisará de:

* **Python 3.x** instalado.
* Biblioteca **PyPDF2**.

## 🔧 Instalação

1.  Clone este repositório ou baixe o arquivo `merge.py`.
2.  Instale a dependência necessária executando o seguinte comando no terminal:

```bash
pip install PyPDF2
````

## 📂 Como usar

### 1\. Preparação dos Arquivos

Para que o script ordene os arquivos corretamente, os nomes dos seus PDFs devem seguir um padrão específico que contenha a string `_venc_` seguida da data no formato `DD-MM-AA`.

**Exemplos de nomes válidos:**

  * `fatura_internet_venc_10-01-24.pdf`
  * `boleto_agua_venc_05-02-24.pdf`
  * `contrato_venc_12-12-23.pdf`

> **Nota:** Arquivos que não seguirem esse padrão serão colocados no início do documento final (considerados como data antiga).

### 2\. Execução

Coloque o arquivo `merge.py` na mesma pasta onde estão os seus arquivos PDF e execute:

```bash
python merge.py
```

### 3\. Resultado

  * Um novo arquivo chamado **`documento_final.pdf`** será criado na mesma pasta.
  * O terminal exibirá a lista de arquivos na ordem em que foram mesclados.

## 📝 Exemplo de Estrutura

Imagine a seguinte pasta:

```text
/minha-pasta
│
├── merge.py
├── conta_luz_venc_20-02-24.pdf
└── aluguel_venc_05-01-24.pdf
```

Ao rodar o script, o **`documento_final.pdf`** terá a seguinte ordem de páginas (ordenado por data):

1.  `aluguel_venc_05-01-24.pdf` (Janeiro)
2.  `conta_luz_venc_20-02-24.pdf` (Fevereiro)

## ⚠️ Tratamento de Erros

  * Se o script não encontrar arquivos PDF, ele avisará e encerrará.
  * Se a biblioteca `PyPDF2` não for encontrada, uma mensagem amigável com o comando de instalação será exibida.

-----

Desenvolvido para automação de tarefas administrativas.
