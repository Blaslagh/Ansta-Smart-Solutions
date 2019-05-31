#ZADANIE 1. GENERATOR KODÓW POCZTOWYCH

def post_codes(first, second):

    first = int(first.replace('-',''))    #converting strings to integers
    second = int(second.replace('-',''))

    for i in range( min([first,second])+1 , max([first, second]) ):   #loop from first nr above bottom limit to last below top limit
        yield(str(i//1000)+'-'+str(i%1000)) #reconverting to strings


#ZADANIE 2. PODANA JEST LISTA ZAWIERAJĄCA ELEMENTY O WARTOŚCIACH 1-n. NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH ELEMENTÓW BRAKUJE

def list_check(lst, n):

    test = list(range(1,n+1))

    for i in lst:
        test.remove(i)

    return test


#ZADANIE 3. NALEŻY WYGENEROWAĆ LISTĘ LICZB OD 2 DO 5.5 ZE SKOKIEM CO 0.5, DANE WYNIKOWE MUSZĄ BYĆ TYPU DECIMAL.

def numbers(a,b):
    from decimal import Decimal
    a, b = Decimal(a), Decimal(b)
    while b>=a:
        yield(a)
        a += Decimal(0.5)        