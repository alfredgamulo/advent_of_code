year := "2024"

_:
    @echo Welcome to {{year}} AoC 🎄
    @just -l -u

install:
    #!/usr/bin/env bash
    poetry install

start day:
    #!/usr/bin/env bash
    mkdir -p {{year}}
    cd {{year}}
    mkdir -p {{day}}
    cd {{day}}
    day=$((10#{{day}}))
    # echo "session=53616c74..." > cookie.txt
    url="https://adventofcode.com/{{year}}/day/${day}"
    curl -b "$(cat {{justfile_directory()}}/cookie.txt)" "${url}/input" > input
    echo $url
    just sample "${url}" > sample
    code input
    code sample

sample url:
    #!.venv/bin/python
    import requests
    from bs4 import BeautifulSoup
    page = requests.get("{{url}}").text.encode('utf-8')
    soup = BeautifulSoup(page, "html.parser")
    print(soup.find('pre').find('code').contents[0].strip())

# Rust
start-rust day:
    #!/usr/bin/env bash
    cd {{year}}/{{day}}
    cargo init --name aoc || true
    cp ../../common/template.rs src/main.rs
    echo "reopen the workspace to this directory"

# Python
start-python day:
    #!/usr/bin/env bash
    cd {{year}}/{{day}}
    cp -n ../../common/template.py main.py
    code main.py

debug-python day input="input":
    #!/usr/bin/env bash
    cd {{year}}/{{day}}
    (time poetry run python main.py {{input}})

run-python day input="input":
    #!/usr/bin/env bash
    cd {{year}}/{{day}}
    (time poetry run python main.py {{input}}) 2>&1 | tee output

lint-python day:
    poetry run black {{year}}/{{day}}/.
    poetry run flake8 {{year}}/{{day}}/.

# Lua

start-lua day:
    #!/usr/bin/env bash
    cd {{year}}/{{day}}
    cp -n ../00/start.lua main.lua || echo "already exists"
    code main.lua

run-lua day input="input":
    #!/usr/bin/env bash
    cd {{year}}/{{day}}
    lua -l inspect main.lua < {{input}}

# Go

start-go day:
    #!/usr/bin/env bash
    cd {{year}}/{{day}}
    cp -n ../../common/template.go main.go || echo "already exists"
    go mod init {{year}}/{{day}}
    code main.go
    cd ../..
    go work use ./{{year}}/{{day}}/

run-go day input="input":
    #!/usr/bin/env bash
    cd {{year}}/{{day}}
    go mod tidy
    go run . < {{input}}
