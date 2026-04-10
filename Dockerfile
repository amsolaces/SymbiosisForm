FROM selenium/standalone-chrome

WORKDIR /app

COPY . .

RUN pip install selenium webdriver-manager

CMD ["python", "test.py"]