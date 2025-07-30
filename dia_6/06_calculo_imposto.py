def calc_imposto(preco:float, tx_base:float, **Kwargs):
    imposto =  preco * tx_base

    for i in Kwargs:
        print(i, Kwargs[i])
        imposto += preco * Kwargs[i]

    return imposto

# %%

calc_imposto(100, 0.03, municipio=0.01, estadual=0.005, nacional=0.001)
