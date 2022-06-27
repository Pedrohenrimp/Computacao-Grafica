
def aoCubo(x):
    return x*x*x

def f(x, i, n):
    if i < n:
        f(aoCubo(x), i + 1, n)
    elif i == n:
        print(x)



def raizCubica(x):
    if x < 0:
        x = abs(x)
        raizCubica = x**(1/3)*(-1)
    else:
        raizCubica = x**(1/3)
    return raizCubica


def inversa(x, i, n):
    if i < n:
        inversa(raizCubica(x), i + 1, n)
    elif i == n:
        print(x)

def mostraImagem(imagem):
    return imagem

def transformaAfim(imagem, a, b, i, n):
    if i < n:
        imagem.resize(a)
        imagem.translate(b)
        transformaAfim(imagem, i + 1, n)
    elif i == n:
        mostraImagem(imagem)

def pontoDobra(polinomio, imagem):

    return imagem

def realizaDobra(imagem, z):
    return imagem

def transformaPolinomial(imagem, polinomio):
    for i in range(imagem.x.size):
        if not pontoDobra(polinomio, polinomio.y[i]):
            imagem.x[i] = polinomio.y[i]
        else:
            realizaDobra(imagem.x[i], imagem.z)