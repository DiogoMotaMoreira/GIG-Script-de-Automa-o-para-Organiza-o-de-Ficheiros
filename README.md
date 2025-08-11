# Gig 001 – Organizador de Ficheiros

**Status:** Concluido  
**Linguagem:** Python  
**Cliente:** Byte & Order  
**Origem:** Gerado por IA para treino e portefólio  

---

## 📜 Briefing
A "Byte & Order" está cansada de ter pastas desorganizadas no computador. Querem um script que organize automaticamente ficheiros por tipo (imagens, PDFs, vídeos, etc.) dentro de pastas corretas.

---

## 🎯 Objetivos
1. Criar um script (Python, Bash ou outra linguagem à escolha) que:
   - Leia todos os ficheiros de uma pasta
   - Crie subpastas por tipo de ficheiro
   - Mova os ficheiros para as subpastas corretas
2. Testar o script numa pasta com ficheiros variados
3. Guardar o código como entrega final

---

## ▶ Como Executar
1. Instalar dependências

Se ainda não tens, instala as bibliotecas necessárias (Pillow e ReportLab) com:
``` bash
pip install pillow reportlab
```

2. Gerar ficheiros de teste

Executa o script que cria ficheiros aleatórios:
``` bash
python src/criar_ficheiros.py
```
3. Organizar os ficheiros

Depois, executa o script principal para organizar os ficheiros em subpastas dentro de docs/pasta_teste:
``` bash
python src/main.py
```
