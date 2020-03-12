from django.shortcuts import render
from django.http import HttpResponse
import numpy as np

# Create your views here.
from django.views.generic import TemplateView


def home(request):
    return render(request, 'home.html')


def addition(request):
    return render(request, 'matrix.html')
def subtract(request):
    return render(request, 'submat.html')
def multiply(request):
    return render(request, 'multimat.html')
def transpose(request):
    return render(request, 'transmat.html')


def add(request):
    matrixA = []
    a = []
    a.append(int(request.POST['val1']))
    a.append(int(request.POST['val2']))
    a.append(int(request.POST['val3']))
    a.append(int(request.POST['val4']))
    b = []
    b.append(int(request.POST['val5']))
    b.append(int(request.POST['val6']))
    b.append(int(request.POST['val7']))
    b.append(int(request.POST['val8']))
    c = []
    c.append(int(request.POST['val9']))
    c.append(int(request.POST['val10']))
    c.append(int(request.POST['val11']))
    c.append(int(request.POST['val12']))
    d = []
    d.append(int(request.POST['val13']))
    d.append(int(request.POST['val14']))
    d.append(int(request.POST['val15']))
    d.append(int(request.POST['val16']))

    matrixA.append(a)
    matrixA.append(b)
    matrixA.append(c)
    matrixA.append(d)
    matrixB = []
    a1 = []
    a1.append(int(request.POST['v1']))
    a1.append(int(request.POST['v2']))
    a1.append(int(request.POST['v3']))
    a1.append(int(request.POST['v4']))
    b1 = []
    b1.append(int(request.POST['v5']))
    b1.append(int(request.POST['v6']))
    b1.append(int(request.POST['v7']))
    b1.append(int(request.POST['v8']))
    c1 = []
    c1.append(int(request.POST['v9']))
    c1.append(int(request.POST['v10']))
    c1.append(int(request.POST['v11']))
    c1.append(int(request.POST['v12']))
    d1 = []
    d1.append(int(request.POST['v13']))
    d1.append(int(request.POST['v14']))
    d1.append(int(request.POST['v15']))
    d1.append(int(request.POST['v16']))

    matrixB.append(a1)
    matrixB.append(b1)
    matrixB.append(c1)
    matrixB.append(d1)
    x = np.array(matrixA)
    y = np.array(matrixB)
    res = x+y
    return render(request, 'add.html', {'A': res})


def sub(request):
    matrixA = []
    a = []
    a.append(int(request.POST['val1']))
    a.append(int(request.POST['val2']))
    a.append(int(request.POST['val3']))
    a.append(int(request.POST['val4']))
    b = []
    b.append(int(request.POST['val5']))
    b.append(int(request.POST['val6']))
    b.append(int(request.POST['val7']))
    b.append(int(request.POST['val8']))
    c = []
    c.append(int(request.POST['val9']))
    c.append(int(request.POST['val10']))
    c.append(int(request.POST['val11']))
    c.append(int(request.POST['val12']))
    d = []
    d.append(int(request.POST['val13']))
    d.append(int(request.POST['val14']))
    d.append(int(request.POST['val15']))
    d.append(int(request.POST['val16']))

    matrixA.append(a)
    matrixA.append(b)
    matrixA.append(c)
    matrixA.append(d)
    matrixB = []
    a1 = []
    a1.append(int(request.POST['v1']))
    a1.append(int(request.POST['v2']))
    a1.append(int(request.POST['v3']))
    a1.append(int(request.POST['v4']))
    b1 = []
    b1.append(int(request.POST['v5']))
    b1.append(int(request.POST['v6']))
    b1.append(int(request.POST['v7']))
    b1.append(int(request.POST['v8']))
    c1 = []
    c1.append(int(request.POST['v9']))
    c1.append(int(request.POST['v10']))
    c1.append(int(request.POST['v11']))
    c1.append(int(request.POST['v12']))
    d1 = []
    d1.append(int(request.POST['v13']))
    d1.append(int(request.POST['v14']))
    d1.append(int(request.POST['v15']))
    d1.append(int(request.POST['v16']))

    matrixB.append(a1)
    matrixB.append(b1)
    matrixB.append(c1)
    matrixB.append(d1)
    x = np.array(matrixA)
    y = np.array(matrixB)
    res = x - y
    return render(request, 'add.html', {'A': res})


def multi(request):
    matrixA = []
    a = []
    a.append(int(request.POST['val1']))
    a.append(int(request.POST['val2']))
    a.append(int(request.POST['val3']))
    a.append(int(request.POST['val4']))
    b = []
    b.append(int(request.POST['val5']))
    b.append(int(request.POST['val6']))
    b.append(int(request.POST['val7']))
    b.append(int(request.POST['val8']))
    c = []
    c.append(int(request.POST['val9']))
    c.append(int(request.POST['val10']))
    c.append(int(request.POST['val11']))
    c.append(int(request.POST['val12']))
    d = []
    d.append(int(request.POST['val13']))
    d.append(int(request.POST['val14']))
    d.append(int(request.POST['val15']))
    d.append(int(request.POST['val16']))

    matrixA.append(a)
    matrixA.append(b)
    matrixA.append(c)
    matrixA.append(d)
    matrixB = []
    a1 = []
    a1.append(int(request.POST['v1']))
    a1.append(int(request.POST['v2']))
    a1.append(int(request.POST['v3']))
    a1.append(int(request.POST['v4']))
    b1 = []
    b1.append(int(request.POST['v5']))
    b1.append(int(request.POST['v6']))
    b1.append(int(request.POST['v7']))
    b1.append(int(request.POST['v8']))
    c1 = []
    c1.append(int(request.POST['v9']))
    c1.append(int(request.POST['v10']))
    c1.append(int(request.POST['v11']))
    c1.append(int(request.POST['v12']))
    d1 = []
    d1.append(int(request.POST['v13']))
    d1.append(int(request.POST['v14']))
    d1.append(int(request.POST['v15']))
    d1.append(int(request.POST['v16']))

    matrixB.append(a1)
    matrixB.append(b1)
    matrixB.append(c1)
    matrixB.append(d1)
    x = np.array(matrixA)
    y = np.array(matrixB)
    res = x * y
    return render(request, 'add.html', {'A': res})

def trans(request):
    matrixA = []
    a = []
    a.append(int(request.POST['val1']))
    a.append(int(request.POST['val2']))
    a.append(int(request.POST['val3']))
    a.append(int(request.POST['val4']))
    b = []
    b.append(int(request.POST['val5']))
    b.append(int(request.POST['val6']))
    b.append(int(request.POST['val7']))
    b.append(int(request.POST['val8']))
    c = []
    c.append(int(request.POST['val9']))
    c.append(int(request.POST['val10']))
    c.append(int(request.POST['val11']))
    c.append(int(request.POST['val12']))
    d = []
    d.append(int(request.POST['val13']))
    d.append(int(request.POST['val14']))
    d.append(int(request.POST['val15']))
    d.append(int(request.POST['val16']))
    matrixA.append(a)
    matrixA.append(b)
    matrixA.append(c)
    matrixA.append(d)
    x = np.array(matrixA)

    return render(request, 'add.html', {'A': x.transpose()})
