import nltk
import re

Formula = "Constante|Proposicao|FormulaUnaria|FormulaBinaria"  
Constante= "T|F" 
Proposicao= "^[a-z0-9]"
AbreParen= "(\()" 
FechaParen= "(\))" 
OperatorUnario= "¬" 
OperatorBinario= "(\∨)|(\∧)|(\→)|(\↔)" 
expressao = []


def main(): 
  while True:
    testarArquivo()
    print("")
  # print(expressao)

  
def eFormula(tokens):
  return eConstante(tokens) or eProposicao(tokens) or eFormulaUnaria(tokens) or eFormulaBinaria(tokens)

  
def eConstante(tokens):
  if any(item in ("T", "F") for item in tokens[0]):
    expressao.append(tokens[0])
    tokens.pop(0)
    return True


def eProposicao(tokens):
  if re.match("^[a-z0-9]", tokens[0]):
    expressao.append(tokens[0])
    tokens.pop(0)
    return True

      
def eAbreParen(tokens):
  if ("(") in tokens[0]:
    expressao.append(tokens[0])
    tokens.pop(0)
    return True

def eFechaParen(tokens):
  if (")") in tokens[0]:
    expressao.append(tokens[0])
    tokens.pop(0)
    return True


def eOperatorUnario(tokens):
  if ("¬") in tokens[0]:
    expressao.append(tokens[0])
    tokens.pop(0)
    return True


def eOperatorBinario(tokens):
  if any(item in ("∨","∧","→","↔") for item in tokens[0]):
    expressao.append(tokens[0])
    tokens.pop(0)
    return True


def eFormulaUnaria(tokens):
  return eAbreParen(tokens) and eOperatorUnario(tokens) and eFormula(tokens) and eFechaParen(tokens)


def eFormulaBinaria(tokens):
  return eAbreParen(tokens) and eOperatorBinario(tokens) and eFormula(tokens) and eFormula(tokens) and eFechaParen(tokens)


def testarArquivo():
  arquivo = input("Arquivo: ")
  try:
    with open(arquivo) as f:
      numeroExpressoes = f.readline()
      
      for i in range(int(numeroExpressoes)):
        expressao.clear()
        palavra  = f.readline()
  
        lista = []
        for i in palavra.replace(" ", "").strip():
          lista.append(i)
        # print(lista)

        try:
          if any(item in ("∨","∧","→","↔") for item in lista):
            if (eFormulaBinaria(lista)):
              print("valido")
            else:
              print("invalido")
          else:
            if (eFormulaUnaria(lista)):
              print("valido")
            else:
              print("invalido")
        except:
          print("invalido")
  except:
    print("Arquivo invalido!")

main()
