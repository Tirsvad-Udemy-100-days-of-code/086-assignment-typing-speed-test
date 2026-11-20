# Linux image for graphical tests and screenshots. The window opens on a virtual
# display (Xvfb), so the host desktop is never used.
FROM python:3.13
RUN apt-get update \
    && apt-get install -y --no-install-recommends xvfb xauth fonts-dejavu-core imagemagick \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
