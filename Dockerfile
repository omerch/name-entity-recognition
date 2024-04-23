FROM python:3.12-slim-bullseye

RUN pip install --upgrade pip

# add non-root user
RUN adduser worker
USER worker
WORKDIR /home/worker

# copying requirements
COPY --chown=worker:worker ./requirements.txt /home/worker/requirements.txt
# installing requirements
RUN pip install --no-cache-dir --upgrade -r /home/worker/requirements.txt

ENV PATH="/home/worker/.local/bin:${PATH}"
# copying application files
COPY --chown=worker:worker ./app /home/worker/app

CMD ["uvicorn", "app.main:fastapi_app", "--host", "0.0.0.0", "--port", "8000"]

EXPOSE 8000

