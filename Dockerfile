FROM python:3.11-slim-bookworm as build
RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  build-essential gcc
 
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
 
# Install dependencies:
COPY requirements.txt .
RUN pip install --disable-pip-version-check -r requirements.txt
 
 
FROM python:3.11-slim-bookworm
 
# Run the application:
WORKDIR /opt/venv
COPY --from=build /opt/venv ./venv
 
COPY . .
ENV PATH="/opt/venv/venv/bin:$PATH"
ENTRYPOINT ["python", "main.py"]
