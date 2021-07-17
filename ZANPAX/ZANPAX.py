Nome = "Zanpax"
Regiao = "Recife-PE"
Valor_do_projeto = float(56.300)
ISS = float(1.04)
ICMS = float(1.18)
Total = float(1.22)
total_imposto = (Valor_do_projeto * Total)
imposto_recife = (Valor_do_projeto * ISS)
imposto_pernambuco =(Valor_do_projeto * ICMS)
print("Nome: {0} \nRegiao: {1} \nValor do Projeto: {2} \nImposto Recife: {3} \nImposto Pernambuco: {4} \nTotal imposto {5}".format(Nome,Regiao,str(Valor_do_projeto),str(imposto_recife),str(imposto_pernambuco),str(total_imposto) ) )

