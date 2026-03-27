import subprocess
import time
import os
from concurrent.futures import ProcessPoolExecutor

# ESTA FUNÇÃO CHAMA O SEU CÓDIGO ORIGINAL SEM ALTERAR ELE
def rodar_caixa_preta(fatia_in, fatia_out):
    # O comando abaixo é o mesmo que você digitaria no terminal:
    # python conversoremescalacinza.py entrada.ppm saida.ppm
    subprocess.run(["python", "conversoremescalacinza.py", fatia_in, fatia_out])

def executar_paralelo(n_threads, arquivo_original):
    print(f"\n--- 🚀 Iniciando com {n_threads} Processos ---")
    inicio = time.time()

    # 1. LER INFOS DA IMAGEM ORIGINAL (P6)
    with open(arquivo_original, "rb") as f:
        header1 = f.readline() # P6
        dim = f.readline().split()
        largura, altura = int(dim[0]), int(dim[1])
        max_val = f.readline() # 255
        offset_dados = f.tell()

    # 2. DIVIDIR A IMAGEM EM FATIAS
    linhas_por_fatia = altura // n_threads
    fatias_in = []
    fatias_out = []

    with open(arquivo_original, "rb") as f_origem:
        f_origem.seek(offset_dados)
        
        for i in range(n_threads):
            nome_in = f"temp_fatia_{i}.ppm"
            nome_out = f"temp_out_{i}.ppm"
            fatias_in.append(nome_in)
            fatias_out.append(nome_out)

            # Determina quantas linhas esta fatia vai ter
            # (A última fatia pega o resto se a divisão não for exata)
            linhas_atuais = linhas_por_fatia if i < n_threads - 1 else altura - (linhas_por_fatia * i)
            
            # Escreve a fatia com um cabeçalho PPM válido para a "caixa-preta" entender
            with open(nome_in, "wb") as f_fatia:
                f_fatia.write(b"P6\n")
                f_fatia.write(f"{largura} {linhas_atuais}\n".encode())
                f_fatia.write(max_val)
                # Copia os pixels brutos da imagem original
                tamanho_pixels = largura * linhas_atuais * 3
                f_fatia.write(f_origem.read(tamanho_pixels))

    # 3. EXECUTAR EM PARALELO (O CORAÇÃO DO PROJETO)
    with ProcessPoolExecutor(max_workers=n_threads) as executor:
        executor.map(rodar_caixa_preta, fatias_in, fatias_out)

    # 4. JUNTAR AS FATIAS (MERGE)
    arquivo_final = f"resultado_{n_threads}t.ppm"
    with open(arquivo_final, "wb") as f_final:
        # Escreve o cabeçalho original da imagem de 16GB
        f_final.write(b"P6\n")
        f_final.write(f"{largura} {altura}\n".encode())
        f_final.write(max_val)
        
        # Concatena apenas os dados de pixels processados
        for f_saida in fatias_out:
            with open(f_saida, "rb") as fs:
                fs.readline() # Pula P6 da fatia
                fs.readline() # Pula Dimensões da fatia
                fs.readline() # Pula 255 da fatia
                f_final.write(fs.read())

    # 5. LIMPEZA DE ARQUIVOS TEMPORÁRIOS
    for f in fatias_in + fatias_out:
        if os.path.exists(f):
            os.remove(f)

    fim = time.time()
    tempo_total = fim - inicio
    print(f"✅ Finalizado em {tempo_total:.2f} segundos.")
    return tempo_total

if __name__ == "__main__":
    imagem = "imagem_aleatoria_1gb.ppm" # Nome do seu arquivo de 16GB
    
    # Lista de testes (1, 2, 4,