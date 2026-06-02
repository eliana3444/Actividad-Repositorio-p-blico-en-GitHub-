# Modelo de Cascada - Reflexión del equipo

## ¿Qué es el modelo de cascada?
El modelo de cascada es una metodología de desarrollo secuencial donde cada fase
se completa antes de pasar a la siguiente. Normalmente se avanza por etapas como
análisis, diseño, implementación, pruebas y despliegue. Su enfoque ordenado ayuda
a documentar bien, pero vuelve costoso volver atrás cuando aparecen cambios.

## Dificultades encontradas
- Dependencia entre roles: frontend queda bloqueado hasta que backend termina sus entregables.
- Dificultad para hacer cambios cuando una fase ya se consideró cerrada.
- Coordinación de ramas en Git compleja cuando cada integrante debe entregar un solo MR/PR.
- Falta de flexibilidad cuando los errores se descubren tarde en pruebas integradas.
- Retrasos acumulados: si una etapa se atrasa, impacta todo el cronograma del equipo.

## Conclusión
El modelo de cascada funciona cuando los requisitos son estables y claros desde el inicio.
En proyectos reales, los cambios y hallazgos tardíos son frecuentes, por lo que su rigidez
puede afectar tiempos, coordinación y calidad final del producto.

## Dependencias e instalación
Para ejecutar este proyecto debes tener instalado Python 3 en tu sistema.

Instala las dependencias con:

```bash
python -m pip install openpyxl tabulate
```

## ¿Cómo correr el proyecto?
1. Abre una terminal en la raíz del proyecto.
2. Ejecuta el programa principal:

```bash
python main.py
```

3. Usa el menú en consola:
- Opción 1: listar productos.
- Opción 2: buscar producto por ID.
- Opción 3: salir del programa.
