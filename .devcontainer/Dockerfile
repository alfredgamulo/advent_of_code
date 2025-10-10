# Base image with Rust and Debian
FROM mcr.microsoft.com/devcontainers/rust:latest

# Set noninteractive mode for apt
ENV DEBIAN_FRONTEND=noninteractive

# Update and install dependencies
RUN apt-get update && apt-get install -y \
    curl gnupg2 lsb-release ca-certificates build-essential \
    python3 python3-pip python3-venv \
    && ln -s /usr/bin/python3 /usr/bin/python \
    && rm -rf /var/lib/apt/lists/*

# Install Rust WASI target
RUN rustup target add wasm32-wasip1

# Switch to non-root user
USER vscode

ENV PATH="/home/vscode/.local/bin:${PATH}"

RUN pip3 install --break-system-packages pipx && \
    pipx ensurepath && \
    pipx install black && \
    pipx install flake8 && \
    pipx install poetry

# Install Just (a handy command runner)
RUN curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to /home/vscode/.local/bin

# VS Code extensions (installed via devcontainer.json, not Dockerfile)
# These are handled by VS Code automatically when the container starts.

# Default shell
CMD [ "bash" ]
