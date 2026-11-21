# 🅿️ Calculadora de parqueadero

Calcula cuánto se cobra en un parqueadero según el tipo de vehículo y las horas de permanencia, aplicando un **tope diario** y clasificando la estadía.

**Dos versiones:**
- `parqueadero.py`: programa de consola en Python.
- `index.html`: versión web interactiva (HTML, CSS y JavaScript), con tarifas ajustables.

## Reglas
| Vehículo | Tarifa por hora | Tope diario |
|---|---|---|
| Motocicleta | $2.000 | $12.000 |
| Automóvil | $4.000 | $24.000 |

- Permanencia: 1–2 h **corta**, 3–5 h **media**, 6–24 h **prolongada**.
- Si el valor por horas supera el tope, se cobra solo el tope.
- Valida entradas: tipo inválido, horas fuera de 1–24 o texto no numérico.

## Cómo correrlo
```bash
python parqueadero.py
```
Para la versión web, abre `index.html` en el navegador.

## Autor
Sebastián Serrato Ramírez, estudiante de Ingeniería Electrónica (Neiva, Colombia).
