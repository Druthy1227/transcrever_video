import whisper
import torch
import os
import time
import sys

# Extensões que o script vai procurar
EXTENSOES_ACEITAS = ('.mp4', '.mp3', '.wav', '.m4a', '.mkv')

def verificar_gpu():
    print("🔍 Verificando hardware...")
    if torch.cuda.is_available():
        print(f"🚀 NVIDIA DETECTADA: {torch.cuda.get_device_name(0)}")
        return "cuda"
    else:
        print("⚠️ GPU não detectada. Usando CPU.")
        return "cpu"

def perguntar_configuracao():
    print("\n--- CONFIGURAÇÃO DE TRANSCRIÇÃO ---")
    print("[1] Apenas PORTUGUÊS (Ignora outros idiomas)")
    print("[2] Apenas INGLÊS (Ignora outros idiomas)")
    print("[3] Traduzir tudo para INGLÊS (Feature de Tradução)")
    print("[4] 🌎 MÚLTIPLOS IDIOMAS (Transcreve exatamente o que for falado)")
    
    while True:
        escolha = input(">> Escolha uma opção: ").strip()
        
        if escolha == "1":
            print("🔒 Configurado: Forçar Português.")
            # prompt ajuda a corrigir pontuação em PT
            return "pt", "transcribe", "O áudio é em português." 
        
        elif escolha == "2":
            print("🔒 Configurado: Forçar Inglês.")
            return "en", "transcribe", "The audio is in English."
            
        elif escolha == "3":
            print("🇺🇸 Configurado: Traduzir áudio para Inglês.")
            return None, "translate", None
            
        elif escolha == "4":
            print("🌎 Configurado: Modo Misto (Detectar mudança de idioma).")
            # O prompt abaixo é o segredo. Ele avisa a IA para não traduzir.
            prompt_misto = "This audio contains a mix of languages. Transcribe exactly what is spoken in each language."
            return None, "transcribe", prompt_misto
            
        print("❌ Opção inválida.")

def transcrever_tudo():
    # 1. Configurações iniciais
    device = verificar_gpu()
    idioma_escolhido, tarefa_escolhida, prompt_inicial = perguntar_configuracao()
    
    # --- MUDANÇA IMPORTANTE ---
    # Para múltiplos idiomas, o 'small' erra muito.
    # O 'medium' é o ideal. Se ficar lento demais, volte para 'small'.
    modelo_tipo = "medium" 
    
    print(f"\n🧠 Carregando modelo '{modelo_tipo}'... (Isso exige mais VRAM)")
    try:
        model = whisper.load_model(modelo_tipo, device=device)
    except:
        print("⚠️ Memória insuficiente para 'medium'. Tentando 'small'...")
        model = whisper.load_model("small", device=device)

    # 2. Listar arquivos
    arquivos = [f for f in os.listdir('.') if f.lower().endswith(EXTENSOES_ACEITAS)]
    
    if not arquivos:
        print("❌ Nenhum arquivo de mídia encontrado na pasta.")
        return

    print(f"\n📂 Encontrados {len(arquivos)} arquivos.\n")

    # 3. Loop de Processamento
    for i, arquivo in enumerate(arquivos, 1):
        nome_txt = os.path.splitext(arquivo)[0] + ".txt"
        
        if os.path.exists(nome_txt):
            print(f"⏭️  [{i}/{len(arquivos)}] '{arquivo}' já existe. Pulando.")
            continue

        print(f"🎙️  [{i}/{len(arquivos)}] Processando: '{arquivo}'...")
        inicio = time.time()
        
        try:
            use_fp16 = True if device == "cuda" else False
            
            # Aqui passamos o 'initial_prompt' que faz a mágica
            result = model.transcribe(
                arquivo, 
                fp16=use_fp16, 
                language=idioma_escolhido, 
                task=tarefa_escolhida,
                initial_prompt=prompt_inicial
            )
            
            with open(nome_txt, "w", encoding="utf-8") as f:
                f.write(result["text"])
            
            tempo = time.time() - inicio
            print(f"✅ Concluído em {tempo:.1f}s.")
            
        except Exception as e:
            print(f"❌ Erro ao processar '{arquivo}': {e}")
            # Se der erro de memória no meio, avisa
            if "CUDA out of memory" in str(e):
                print("\n⚠️ ERRO DE MEMÓRIA: O modelo 'medium' é pesado.")
                print("Edite o código e mude 'modelo_tipo' para 'small'.")
                sys.exit()

    print("\n🎉 Finalizado!")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    transcrever_tudo()
    input("Pressione Enter para sair...")

    