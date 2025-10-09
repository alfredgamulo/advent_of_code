# Base image with Rust and Debian Bookworm
FROM mcr.microsoft.com/devcontainers/rust:1-1-bookworm

# Set noninteractive mode for apt
ENV DEBIAN_FRONTEND=noninteractive

# Update and install dependencies
RUN apt-get update && apt-get install -y \
    curl gnupg2 lsb-release ca-certificates build-essential \
    python3 python3-pip python3-venv \
    && rm -rf /var/lib/apt/lists/*

# Install Rust WASI target
RUN rustup target add wasm32-wasip1

# Optional: install Python tools (e.g., pipx, black, flake8)
RUN pip3 install --break-system-packages --upgrade pip && \
    pip3 install --break-system-packages pipx && \
    pipx ensurepath && \
    pipx install black && \
    pipx install flake8

# Install Poetry
USER vscode
RUN curl -sSL https://install.python-poetry.org | python3 -

# Install Just (a handy command runner)
RUN curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to /home/vscode/.local/bin

# VS Code extensions (installed via devcontainer.json, not Dockerfile)
# These are handled by VS Code automatically when the container starts.

# Default shell
CMD [ "bash" ]
