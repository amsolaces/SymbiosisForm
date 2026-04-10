FROM selenium/standalone-chrome

WORKDIR /app

COPY . .

RUN pip install selenium

CMD ["python3", "test.py"]