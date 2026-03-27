import matplotlib.pyplot as plt
import numpy as np

# --- DADOS REAIS DO SEU EXPERIMENTO (COPIE EXATAMENTE ASSIM) ---
threads = [1, 2, 4, 8, 12]
tempos = [171.11, 247.07, 139.59, 148.13, 179.01]
# O Speedup é calculado como: Tempo_Serial / Tempo_Paralelo
speedups = [171.11 / t for t in tempos]
# A Eficiência é calculada como: Speedup / Número de Threads
eficiencias = [s / t for s, t in zip(speedups, threads)]

# Configuração visual padrão para todos os gráficos
plt.rcParams.update({'font.size': 12, 'figure.figsize': (10, 6)})

# ==============================================================================
# GRÁFICO 1: TEMPO DE EXECUÇÃO TOTAL
# ==============================================================================
plt.figure() # Cria uma nova figura
plt.plot(threads, tempos, marker='o', color='royalblue', linestyle='-', linewidth=2.5, markersize=8)

# Títulos e Labels
plt.title('Gráfico 1: Tempo Total de Execução (Serial + Paralelo)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Número de Threads (Nº de Processos Simultâneos)', fontsize=14)
plt.ylabel('Tempo Total (segundos)', fontsize=14)

# Ajustes do eixo X (para mostrar exatamente os números de threads)
plt.xticks(threads)
plt.grid(True, linestyle='--', alpha=0.6)

# Adicionar rótulos de dados (os valores exatos acima dos pontos)
for i, txt in enumerate(tempos):
    plt.annotate(f'{txt:.2f}s', (threads[i], tempos[i]), textcoords="offset points", xytext=(0,12), ha='center', fontweight='bold')

# Salvar e fechar
plt.tight_layout()
plt.savefig('1_tempo_execucao.png', dpi=300) # dpi=300 garante alta qualidade
print("✅ Gráfico de Tempo gerado: '1_tempo_execucao.png'")
plt.close() # Fecha a figura para não sobrepor no próximo gráfico


# ==============================================================================
# GRÁFICO 2: SPEEDUP ALCANÇADO
# ==============================================================================
plt.figure()
plt.plot(threads, speedups, marker='s', color='forestgreen', linestyle='-', linewidth=2.5, markersize=8, label='Speedup Medido')

# Linha de referência do Speedup Ideal (Linear)
plt.plot(threads, threads, color='tomato', linestyle='--', linewidth=2, label='Speedup Ideal (Linear)')

# Títulos e Labels
plt.title('Gráfico 2: Speedup Alcançado vs. Ideal', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Número de Threads', fontsize=14)
plt.ylabel('Speedup (Fator de Aceleração)', fontsize=14)

# Ajustes
plt.xticks(threads)
# Definir o limite do eixo Y para garantir que a linha ideal apareça
plt.ylim(0, max(threads) + 1)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12)

# Adicionar rótulos de dados
for i, txt in enumerate(speedups):
    plt.annotate(f'{txt:.2f}x', (threads[i], speedups[i]), textcoords="offset points", xytext=(0,12), ha='center', fontweight='bold', color='forestgreen')

# Salvar e fechar
plt.tight_layout()
plt.savefig('2_speedup.png', dpi=300)
print("✅ Gráfico de Speedup gerado: '2_speedup.png'")
plt.close()


# ==============================================================================
# GRÁFICO 3: EFICIÊNCIA DO USO DE RECURSOS
# ==============================================================================
plt.figure()
# Usaremos um gráfico de barras para eficiência, fica mais claro
bars = plt.bar(threads, eficiencias, color='purple', alpha=0.7, edgecolor='black', width=0.8)

# Títulos e Labels
plt.title('Gráfico 3: Eficiência do Uso de Processadores', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Número de Threads', fontsize=14)
plt.ylabel('Eficiência (Speedup / N_Threads)', fontsize=14)

# Ajustes
plt.xticks(threads)
plt.ylim(0, 1.1) # Eficiência vai de 0 a 1 (ou 0% a 100%)
plt.grid(True, axis='y', linestyle='--', alpha=0.5)

# Adicionar rótulos de dados (formatado como porcentagem)
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.1%}',
             ha='center', va='bottom', fontweight='bold', fontsize=11)

# Salvar e fechar
plt.tight_layout()
plt.savefig('3_eficiencia.png', dpi=300)
print("✅ Gráfico de Eficiência gerado: '3_eficiencia.png'")
plt.close()

print("\n🚀 Todos os 3 gráficos foram gerados com sucesso na sua pasta!")