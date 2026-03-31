# LAB 1 – Scanner, Analisador Léxico, Regexp e Autômato Finito

**Faculdade:** PUC-SP  
**Curso:** Ciência da Computação  
**Disciplina:** Compiladores    
- Lucas Ferri dos Santos  

---

## 📌 Sobre o Laboratório

Este repositório contém as entregas referentes ao LAB 1, voltadas à compreensão e implementação da primeira fase de um compilador: o **Analisador Léxico (Scanner)**.  
As atividades exploram desde o conceito de **fluxo de caracteres** até a construção de um **mini-scanner estruturado** e a utilização de expressões regulares para tokenização.

---

## 💻 Atividades Realizadas

### Atividade 1: Bash no Terminal Linux (Simulando o "fluxo de entrada")

- Criamos um script Bash (`scanner_simples.sh`) executado via terminal, que lê um arquivo de código fonte (`exemplo.c`) linha a linha.
- O script utiliza o comando `tr` (ou leitura direta) para tratar o fluxo de caracteres, simulando como o compilador enxerga o **character stream** antes da tokenização.
- Tokens identificados: identificadores, números, operadores e símbolos desconhecidos.

**Evidência:**  
![Print Terminal Scanner](Evidencias/Atv1_print.png)

---

### Atividade 2: Expressões Regulares (Regex)

- Utilizamos a ferramenta online [Regex101](https://regex101.com/) para modelar expressões regulares capazes de identificar os tokens de uma linguagem simples.

#### Regex Unificada

```regex
[a-zA-Z_][a-zA-Z0-9_]*|\d+|[=+\-*]
```

**Evidencia:**
![Print Regex Unificada](Evidencias/Atv2_print.png)

**Extras**
expressões regulares para validar dados reais:

CPF: ```\d{3}\.\d{3}\.\d{3}-\d{2}```

Telefone (Brasil): ``` \(\d{2}\)\s\d{4,5}-\d{4}```

E-mail: ```[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}```

![Print Extras](Evidencias/CPF_print.png)
