
def triSelection(tabMoyenne):
    for i in range(len(tabMoyenne)-1):
        plusPetit = i
        for k in range(i+1, len(tabMoyenne)):
            if(tabMoyenne[k] < tabMoyenne[plusPetit]):
                plusPetit = k       
        tmp=tabMoyenne[i]
        tabMoyenne[i]=tabMoyenne[plusPetit]
        tabMoyenne[plusPetit]=tmp
    print("Tri par Selection:",tabMoyenne)






def triInsertion(tab):
    for i in range(1, len(tab)):
        tmp=tab[i]
        k=i
        while (k>0 and tab[k-1]>tmp):
            tab[k] = tab[k-1]
            k-=1
        tab[k]=tmp
    print("Tri par Insertion:", tab)
    return(tab)

    
tabmoyenne = [1000, 1400, 5000]

triSelection(tabmoyenne)

triInsertion(tabmoyenne)
def totalPrice(tabmoyenne):
    total=0
    for i in range(len(tabmoyenne)-1):
        total=total+tabmoyenne[i]
    return total

totalPrice(tabmoyenne)
def calculListePrice(tab, discount):
    tab = triInsertion(tab)
    MaxPrix = tab[-1]
    reduction= MaxPrix * discount / 100
    TotalPrice = totalPrice(tab) + reduction
    print("le Prix Max est:",MaxPrix,"La reduction est :",reduction,"et le Prix Total est:",TotalPrice)
    return TotalPrice

    
calculListePrice(tabmoyenne,10)

