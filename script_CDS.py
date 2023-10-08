# Importar o módulo sys para trabalhar com argumentos da linha de comando
import sys

# Verificar o número de argumentos fornecidos
if len(sys.argv) != 8:
    print("Erro: Forneça exatamente sete argumentos. Uma sequência de DNA e seis números inteiros.")
    sys.exit(1)

# Atribuir argumentos às variáveis correspondentes
dna_seq = sys.argv[1]
n1, n2, n3, n4, n5, n6 = sys.argv[2:8]

# Verificar se os argumentos fornecidos são do tipo correto
if not (n1.isdigit() and n2.isdigit() and n3.isdigit() and n4.isdigit() and n5.isdigit() and n6.isdigit() and 
        0 < int(n1) <= len(dna_seq) and 0 < int(n2) <= len(dna_seq) and 0 < int(n3) <= len(dna_seq) and 
        0 < int(n4) <= len(dna_seq) and 0 < int(n5) <= len(dna_seq) and 0 < int(n6) <= len(dna_seq)):
    print("Erro: Certifique-se de que forneceu números inteiros válidos para as coordenadas n1 a n6.")
    sys.exit(1)

# Converter coordenadas para inteiros
n1, n2, n3, n4, n5, n6 = int(n1), int(n2), int(n3), int(n4), int(n5), int(n6)

# Extrair as sequências de CDS
cds1 = dna_seq[n1-1:n2]
cds2 = dna_seq[n3-1:n4]
cds3 = dna_seq[n5-1:n6]

# Verificar a validade das sequências de CDS
if cds1.startswith("ATG") and (cds3.endswith("TAG") or cds3.endswith("TAA") or cds3.endswith("TGA")):
    print("Sequência resultante após concatenar CDS1, CDS2 e CDS3:", cds1 + cds2 + cds3)
else:
    print("As sequências CDS1 e/ou CDS3 não atendem aos critérios especificados.")

