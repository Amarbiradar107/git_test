FROM python:3.11-slim

# optional: install chrome if you need it for your selenium tests
RUN apt-get update && \
    apt-get install -y wget gnupg2 && \
    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" \
        > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy the rest of the repository
COPY . .

# default command when the container is run
CMD ["pytest", "Optima_Automation", "-vs"]