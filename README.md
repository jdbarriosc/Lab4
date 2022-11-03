# Lab4
Para ejecutar el servidor y poderse comunicar desde postman con este se debe hacer pull o fork del repositorio a la maquina loca.
Abrir la consola cmd.
Instalar las dependencias.
- pip install fastapi
- pip install joblib
- pip install pandas
- pip install scikit-learn==1.0.2
- pip install "uvicorn[standard]"

Para finalmente correr el servidor:
- uvicorn main:app --reload

Los requests se enviaran al http://127.0.0.1:8000/
