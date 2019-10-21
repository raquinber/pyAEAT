#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Creador simple de modelos AEAT en python para pyme."""

__version__ = "0.0.0"

import random
import requests
from lxml import html
import calendar
import datetime
import time

# https://www.agenciatributaria.es/static_files/AEAT/Contenidos_Comunes/La_Agencia_Tributaria/Ayuda/Disenyos_de_registro/Ayudas/Trimestrales_Mensuales/DR303e12v11.pdf
# https://www.agenciatributaria.es/AEAT.internet/Inicio/Ayuda/Disenos_de_registro/Modelos_300_al_399/Modelos_300_al_399.shtml

class pyAEAT():
    """pyAEAT class."""

    def __init__(self):
        """First init class."""
        self.savepages = True

    def main(self):
        """Main function."""
        self.anytri = input('Introduce año y el trimestre, ejemplo: 20193T\n')
        self.NIFempresadesarrollo = 'Q2826000H'
        self.tipodeclaracion = input('El tipo de declaración puede ser: '
                                     + 'C (solicitud de compensación) '
                                     + 'D (devolución) '
                                     + 'G (cuenta corriente tributaria-ingreso) '
                                     + 'I (ingreso) '
                                     + 'N (sin actividad/resultado cero) '
                                     + 'V (cuenta corriente tributaria - devolución), '
                                     + 'ejemplo: I\n')
        self.NIF = input('Introduce el NIF para identificar la empresa, ejemplo: BXXXXXXXX\n')
        aux = input('Apellidos + nombre o razón social, ejemplo: RAQUINBER, S.L.\n')
        self.razonsocial = aux.ljust(80) # apellido + nombre
        self.bi21 = float(input('Base imponible del 21%, ejemplo: 1000.00\n'))
        self.iva21 = float(input('IVA devengado del 21%, ejemplo: 210.00\n'))
        self.baseimponible10 = float(input('Base imponible del 10%, ejemplo: (vacío 0.00)\n'))
        self.iva10 = float(input('IVA devengado del 10%, ejemplo: (vacío 0.00)\n'))
        # EMITIDAS
        self.devengado = self.iva10 + self.iva21
        # RECIBIDAS
        self.deducible10 = float(input('IVA deducible del 10%, ejemplo: (vacío 0.00)\n'))
        self.deducible21 = float(input('IVA deducible del 21%, ejemplo: (vacío 0.00)\n'))
        self.deducible = round(self.deducible10 + self.deducible21, 2)
        self.baseimponibleDedu = float(input('IVA total deducible, ejemplo: (vacío 0.00)\n'))
        self.exonerado390 = '0'
        # FINAL
        self.resultado = round(self.devengado - self.deducible, 2)
        self.content = ('<T3030' + self.anytri + '0000><AUX>' + (' ' * 70) +
                        '1.05    ' + self.NIFempresadesarrollo + (' ' * 213) +
                        '</AUX>')
        dp30301 = ('<T30301000> ' + self.tipodeclaracion + self.NIF +
                   self.razonsocial + self.anytri + '232200000000 2222' +
                   ('0' * 17) + '00400' + ('0' * 17) +
                   ('0' * 17) + '01000' + ('0' * 17) +
                   self.addceros(self.bi21, 17) + '02100' + self.addceros(self.iva21, 17) +
                   ('0' * 17 * 7) + '00520' + ('0' * 17 * 2) +
                   '00140' + ('0' * 17 * 2) + '00000' +
                   ('0' * 17 * 3) + self.addceros(self.devengado, 17) +
                   self.addceros(self.baseimponibleDedu, 17) +
                   self.addceros(self.deducible, 17) + ('0' * 17 * 15) +
                   self.addceros(self.deducible, 17) + self.addceros(self.resultado, 17) + '022' +
                   self.exonerado390 +
                   (' ' * 578) + (' ' * 13) + '</T30301000>')
        if len(dp30301) == 1442:
            print('dp30301 OK')
        else:
            print('dp30301 con ERROR')
        self.content += dp30301
        dp30303 = ('<T30303000>' + ('0' * 17 * 8) + self.addceros(self.resultado, 17) +
                   '10000' + ('0' * 4) + self.addceros(self.resultado, 17) +
                   ('0' * 17 * 3) + self.addceros(self.resultado, 17) +
                   ('0' * 17) + self.addceros(self.resultado, 17) +
                   # 22 - 26
                   (' ' * 60) + ('0    ' * 6) + ' ' + ('0' * 17 * 9) + ('0' * 21) +
                   ('0' * 17 * 6) + ('0' * 5) + (' ' * 463) + '</T30303000>')
        if len(dp30303) == 1139:
            print('dp30303 OK')
        else:
            print('dp30303 con ERROR')
        self.content += dp30303
        self.content += '</T3030' + self.anytri + '0000>'
        self.selecSesion()

    def selecSesion(self):
        """selecSesion url."""
        if self.savepages:
            with open(self.anytri + '.txt', 'wb') as fr:
                b = self.content.encode('utf-8')
                fr.write(b)

    def addceros(self, input, len=7):
        """Add ceros."""
        a = "{:.2f}".format(input)
        b = str(a).replace('.', '')
        output = b.zfill(len)
        return output

    def blancos(self, len):
        return (' ' * len)


if __name__ == '__main__':
    c = pyAEAT()
    c.main()
