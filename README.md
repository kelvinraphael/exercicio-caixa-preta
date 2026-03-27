<<<<<<< HEAD
# exercicio-caixa-preta
=======
# Relatório da Atividade 3 – Paralelização de Imagem (Caixa-Preta)

**Disciplina:** Concorrência e Paralelismo  
**Aluno:** [Kelvin Raphael de souza pereira]  
**Dados do experimento:** Conversão de imagem PPM (16 GB) para escala de cinza utilizando fatiamento e processos paralelos.

---

## 1. Descrição do Problema
O problema consiste em processar uma imagem de ultra-alta resolução (75672 x 75672 pixels) no formato PPM, totalizando aproximadamente 16 GB em disco. O desafio principal é realizar a conversão para escala de cinza tratando o script original (`conversoremescalacinza.py`) como uma **caixa-preta**, sem alterar seu código interno. 

* **Objetivo da paralelização:** Reduzir o tempo de execução através da decomposição de domínio (fatiamento da imagem).
* **Complexidade aproximada:** O algoritmo tem complexidade $O(n)$, onde $n$ é o número total de pixels da imagem.

---

## 2. Ambiente Experimental
| Item | Descrição |
| :--- | :--- |
| **Processador** | [Insira seu processador aqui, ex: Core i5 12th Gen] |
| **Núcleos** | [Insira o número de núcleos] |
| **Memória RAM** | 16 GB |
| **Sistema Operacional** | Windows 11 |
| **Linguagem utilizada** | Python 3.13 |
| **Biblioteca** | `subprocess` e `concurrent.futures` |

---

## 3. Metodologia de Testes
* **Medição de tempo:** Utilizado `time.time()` antes e depois da execução.
* **Entrada utilizada:** Arquivo `imagem_aleatoria_1gb.ppm` com 16 GB de tamanho.
* **Estratégia:** A imagem foi dividida em $N$ fatias horizontais. Cada fatia recebeu um cabeçalho PPM temporário para ser processada individualmente. Ao final, os resultados foram concatenados binariamente (Merge).
* **Configurações testadas:** 1 processo (serial), 2, 4, 8 e 12 processos.

---

## 4. Resultados Experimentais

### 4.1 Tabela de Tempos de Execução
| Nº de Processos | Tempo (s) |
| :--- | :--- |
| 1 (Serial) | 171.11 |
| 2 | 247.07 |
| 4 | 139.59 |
| 8 | 148.13 |
| 12 | 179.01 |

### 4.2 Aceleração (Speedup) e Eficiência
| Processos | Speedup | Eficiência |
| :--- | :--- | :--- |
| 1 | 1.00 | 1.00 |
| 2 | 0.69 | 0.34 |
| 4 | 1.23 | 0.30 |
| 8 | 1.16 | 0.14 |
| 12 | 0.96 | 0.08 |

---

## 5. Contagem Consolidada da Imagem
| Métrica | Quantidade |
| :--- | :--- |
| **Resolução** | 75.672 x 75.672 pixels |
| **Tamanho do Arquivo** | ~16 GB |
| **Formato** | PPM (P6) |

---

## 6. Gráficos
*(Nesta seção, devem ser anexadas as imagens: `1_tempo_execucao.png`, `2_speedup.png` e `3_eficiencia.png`)*

---

## 7. Análise dos Resultados
* O tempo de execução apresentou uma anomalia com **2 processos**, sendo superior ao serial. Isso ocorre devido ao alto custo de **I/O (Input/Output)** para fatiar e gravar arquivos temporários de Gigabytes no disco.
* O **desempenho ótimo** foi alcançado com **4 processos**, onde o ganho de processamento da CPU conseguiu superar o overhead de manipulação de arquivos.
* A partir de 8 processos, a **eficiência cai drasticamente**. Isso evidencia que o sistema atingiu o gargalo do barramento de disco (Saturação de I/O).

---

## 8. Conclusão
* A paralelização externa de sistemas "caixa-preta" é uma solução viável para ganho de performance sem alteração de código legado.
* O limite de escalabilidade para arquivos massivos é definido pela **velocidade do armazenamento (SSD/HD)** e não apenas pelo número de núcleos da CPU.
* O uso de 4 processos mostrou-se o ponto de equilíbrio ideal para este hardware específico.
>>>>>>> d4b67b2 (Relatorio final de paralelização)
