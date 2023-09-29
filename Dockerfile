FROM python:3

WORKDIR /tipcalculator/app

COPY TipCalculator.py .
COPY Requirements.txt .

RUN pip install -r Requirements.txt

CMD ["python", "TipCalculator.py"]