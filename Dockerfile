FROM python:3.11-slim

# Install Chrome and dependencies
RUN apt-get update && \
    apt-get install -y wget gnupg2 curl && \
    curl https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor > /usr/share/keyrings/google-linux-keyring.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-linux-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" \
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