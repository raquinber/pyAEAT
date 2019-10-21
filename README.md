# pyAEAT

Creador simple de modelos AEAT en python para pyme

## Aviso

No nos hacemos responsables de cualquier error que pueda tener este software. Usted es responsable de verificar el contenido del mismo previa presentación telemática.

## Características

- Modelo 303 para declaración de IVA trimestral simple

## Ejecución

 - En la línea de comandos: `python pyAEAT.py`

Luego el software irá preguntando lo que necesita para crear el fichero.

Salida:

```
Introduce año y el trimestre, ejemplo: 20193T
20193T
El tipo de declaración puede ser: C (solicitud de compensación) D (devolución) G (cuenta corriente tributaria-ingreso) I (ingreso) N (sin actividad/resultado cero) V (cuenta corriente tributaria - devolución), ejemplo: I
I
Introduce el NIF para identificar la empresa, ejemplo: BXXXXXXXX
BXXXXXXXX
Apellidos + nombre o razón social, ejemplo: RAQUINBER, S.L.
RAQUINBER, S.L.
Base imponible del 21%, ejemplo: 1000.00
1000.00
IVA devengado del 21%, ejemplo: 210.00
210.00
Base imponible del 10%, ejemplo: (vacío 0.00)
0.00
IVA devengado del 10%, ejemplo: (vacío 0.00)
0.00
IVA deducible del 10%, ejemplo: (vacío 0.00)
362.00
IVA deducible del 21%, ejemplo: (vacío 0.00)
56.35
IVA total deducible, ejemplo: (vacío 0.00)
154.25
dp30301 OK
dp30303 OK
```

## Cambios

- Version 0.0.0 primera versión para obtener el modelo 303

## Información de referencia

- https://www.agenciatributaria.es/static_files/AEAT/Contenidos_Comunes/La_Agencia_Tributaria/Ayuda/Disenyos_de_registro/Ayudas/Trimestrales_Mensuales/DR303e12v11.pdf
- https://www.agenciatributaria.es/AEAT.internet/Inicio/Ayuda/Disenos_de_registro/Modelos_300_al_399/Modelos_300_al_399.shtml

## License

GNU General Public License version 2

- https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
- https://choosealicense.com/licenses/gpl-2.0/
- https://opensource.org/licenses/GPL-2.0
