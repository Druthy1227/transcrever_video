````markdown
# 🎙️ Transcritor de Vídeos com IA (GPU Powered)

Este projeto é uma ferramenta de automação em Python para transcrever vídeos e áudios em lote utilizando o modelo **Whisper** (OpenAI).

O sistema foi otimizado para usar **Placas de Vídeo NVIDIA (CUDA)**, garantindo transcrições extremamente rápidas, e inclui suporte para tradução e múltiplos idiomas.

---

## 📂 Estrutura Obrigatória

Para funcionar, sua pasta deve estar organizada exatamente assim:

```text
📁 C:\Seu_Projeto\
│
├── 📁 venv/                     (Ambiente Virtual - criado na instalação)
├── 🐍 transcrever_pasta_toda.py (O script principal)
├── ⚙️ ffmpeg.exe                (Obrigatório: Executável de áudio)
├── 📜 INICIAR.bat               (Atalho para rodar facilmente)
└── 🎬 Seus_Videos.mp4           (Seus arquivos para transcrever)
````

-----

## 🆘 Instalação e Configuração (Do Zero)

Se você acabou de baixar este projeto ou trocou de computador, siga a ordem exata abaixo:

### 1\. Instalar Python 3.11

O projeto requer Python 3.11 para compatibilidade máxima com bibliotecas de áudio.

  * **[Clique aqui para baixar o Python 3.11 (Installer 64-bit)](https://www.google.com/search?q=https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe)**
  * ⚠️ **Importante:** Na primeira tela da instalação, marque a caixa **"Add Python to PATH"**.

### 2\. Configurar o FFmpeg

O FFmpeg é o "motor" que lê os arquivos de vídeo. Sem ele, o script não funciona.

1.  Baixe o **[FFmpeg Release Essentials (.zip)](https://www.google.com/search?q=https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip)**.
2.  Abra o arquivo ZIP baixado e entre na pasta `bin`.
3.  Copie o arquivo **`ffmpeg.exe`**.
4.  Cole-o na **raiz da pasta deste projeto** (ao lado do arquivo `.py`).

### 3\. Criar o Ambiente Virtual

Abra o terminal na pasta do projeto e rode o comando abaixo para criar um ambiente isolado com a versão correta do Python:

```bash
py -3.11 -m venv venv
```

### 4\. Instalar as Bibliotecas de IA

Agora, ative o ambiente e instale o suporte a NVIDIA e o Whisper. Copie e cole os comandos:

```bash
# 1. Ativar o ambiente
venv\Scripts\activate

# 2. Instalar PyTorch com suporte a GPU NVIDIA (CUDA 12.1)
pip install torch torchvision torchaudio --index-url [https://download.pytorch.org/whl/cu121](https://download.pytorch.org/whl/cu121)

# 3. Instalar o Whisper e ferramentas de vídeo
pip install openai-whisper yt-dlp
```

### 5\. Criar Atalho de Execução

Para não precisar digitar comandos no futuro, crie um arquivo chamado **`INICIAR.bat`** na pasta do projeto com o seguinte conteúdo:

```batch
@echo off
echo Iniciando Transcritor...
call venv\Scripts\activate
python transcrever_pasta_toda.py
pause
```

-----

## 📖 Como Utilizar

1.  **Prepare:** Coloque seus vídeos (`.mp4`, `.mkv`, `.mov`) ou áudios (`.mp3`) na mesma pasta do script.
2.  **Execute:** Dê dois cliques no arquivo **`INICIAR.bat`**.
3.  **Escolha o Modo:** Digite o número da opção desejada no menu:

| Opção | Modo | Quando usar? |
| :--- | :--- | :--- |
| **[1]** | **Apenas PORTUGUÊS** | **(Recomendado)** Para vídeos em português. Ignora ruídos ou termos estrangeiros. |
| **[2]** | **Apenas INGLÊS** | Para conteúdos 100% em inglês. |
| **[3]** | **Traduzir para INGLÊS** | Ouve qualquer idioma (Chinês, Alemão, etc.) e gera o texto traduzido para Inglês. |
| **[4]** | **🌎 MÚLTIPLOS IDIOMAS** | Para vídeos onde o falante troca de idioma (ex: fala PT e depois EN). *Usa modelo 'medium'.* |

4.  **Pronto:** O script gerará arquivos `.txt` com o mesmo nome dos vídeos.

-----

## 🔧 Ajustes Avançados (Performance)

O script vem configurado para rodar rápido na maioria das GPUs. Se quiser alterar a precisão, edite o arquivo `transcrever_pasta_toda.py` e mude a variável `modelo_tipo`:

  * `"base"`: Muito rápido, baixa precisão (\~1GB VRAM).
  * `"small"`: **(Padrão)** Bom equilíbrio (\~2GB VRAM).
  * `"medium"`: Alta precisão, mais lento (\~5GB VRAM).
  * `"large"`: Precisão máxima, bem lento (\~10GB VRAM).

-----

## 🛠️ Solução de Problemas

**Erro: `WinError 2` / `O sistema não pode encontrar o arquivo`**

> Você esqueceu o Passo 2. Baixe o `ffmpeg.exe` e coloque na pasta do projeto.

**Erro: `ModuleNotFoundError: No module named 'torch'`**

> Você não está usando o ambiente virtual. Use o arquivo `INICIAR.bat` para rodar.

**Erro: `CUDA out of memory`**

> Sua placa de vídeo não aguentou o modelo escolhido (geralmente no modo Múltiplos Idiomas). Edite o código e mude para `"small"`.

```
```
