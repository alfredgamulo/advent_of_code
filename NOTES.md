```
brew install just pyenv openssl@3

echo 'eval "$(pyenv init --path)"' >> ~/.zprofile
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

env PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.11
pyenv local 3.11

curl -sSL https://install.python-poetry.org | python3

cat << EOF > poetry.toml
[virtualenvs]
in-project = true
system-packages = true
EOF

poetry env use 3.11
poetry init # creates pyproject.toml
poetry install

poetry add --dev black flake8
```
