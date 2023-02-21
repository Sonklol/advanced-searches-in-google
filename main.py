import webbrowser
import os
from art import *
import time

linux = 'clear'
windows = 'cls'

xbusqueda=''
palabras_clave=''
xpalabras_clave=''
site=''
xsite=''
filetype=''
xfiletype=''
precios=''
primer_valor=''
segundo_valor=''
xbusqueda_paralela=''
busqueda_paralela=''

def marca_agua():
    os.system ([linux, windows][os.name == 'nt'])
    tprint('ADVANCED SEARCH')
    tprint('ENGINE - GOOGLE')
    print('Creada por Sonk    ----    github.com/sonklol')
    print('Si no quieres realizar un apartado, simplemente pulsa enter\n')
marca_agua()

while xbusqueda == '':
    xbusqueda = str(input('Introduce la búsqueda: [Como hacer una calculadora en python] '))
    if xbusqueda == '':
        marca_agua()
        print('ERROR - No puedes continuar sin búsqueda principal')
array_busqueda = xbusqueda.split(' ')
busqueda = str('+'.join(array_busqueda))

xpalabras_clave=(str(input('Introduce las palabras clave: [python, calculadora, sonk] ')))
if xpalabras_clave != '':
    array_palabras_clave = xpalabras_clave.split(', ')
    ypalabras_clave = '%22+%22'.join(array_palabras_clave)
    palabras_clave = str('+'+'%22'+ypalabras_clave+'%22')

xsite=str(input('Introduce una URL: [sonk.es] '))
if xsite != '':
    site=str('+site%3A'+xsite)

xfiletype=str(input('Introduce un formato de archivo para buscar: [pdf] '))
if xfiletype != '':
    filetype=str('+filetype%3A'+xfiletype)

xprimer_valor=str(input('Introduce un número mínimo de precio del producto/servicio: [3] '))
if xprimer_valor != '':
    primer_valor=int(xprimer_valor)
    segundo_valor=int(input('Introduce un número máximo de precio del producto/servicio: [10] '))
    precios=str('+'+str(primer_valor)+'%E2%82%AC...'+str(segundo_valor)+'%E2%82%AC')

xbusqueda_paralela=str(input('Introduce una búsqueda secundario complementaria: [Como hacer una calculadora en java] '))
if xbusqueda_paralela != '':
    array_busqueda_paralela = xbusqueda_paralela.split(' ')
    busqueda_paralela = str('+'.join(array_busqueda_paralela))
    busqueda_paralela=str('+%7C+'+busqueda_paralela)

marca_agua()

print('BÚSQUEDA: '+xbusqueda+'\nPALABRAS CLAVE: '+xpalabras_clave+'\nDOMINIO: '+xsite+'\nFICHERO: '+xfiletype+'\n'+'PRECIOS: '+str(primer_valor)+'€ - '+str(segundo_valor)+'€'+'\n2A BÚSQUEDA: '+xbusqueda_paralela+'\nURL: https://www.google.com/search?q='+busqueda+palabras_clave+site+filetype+precios+busqueda_paralela)

webbrowser.open('https://www.google.com/search?q='+busqueda+palabras_clave+site+filetype+precios+busqueda_paralela)

print('\nSALIENDO...')
time.sleep(10)