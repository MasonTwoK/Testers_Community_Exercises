FROM python:3.12

COPY . /usr/src/Testers_Community_Exercises

RUN pip install pytest

WORKDIR /usr/src/Testers_Community_Exercises/Pytest_AQA
CMD ["pytest", ".", "-v"]
