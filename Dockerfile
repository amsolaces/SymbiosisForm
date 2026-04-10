<<<<<<< HEAD
FROM selenium/standalone-chrome

WORKDIR /app

COPY . .

RUN pip install selenium

=======
FROM selenium/standalone-chrome

WORKDIR /app

COPY . .

RUN pip install selenium

>>>>>>> a6d49f4f9bf51254ed48dc53d613efb206796e34
CMD ["python3", "test.py"]