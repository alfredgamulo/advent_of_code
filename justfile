year := "2021"

_:
    @just -l -u --list-heading $'Welcome to {{year}} AoC 🎄\n'

start day:
    #!/usr/bin/env bash
    cd {{year}}
    mkdir -p {{day}}
    cd {{day}}
    touch main.py
    day=$((10#{{day}}))
    # echo "session=53616c74..." > cookie.txt
    curl -b "$(cat {{justfile_directory()}}/cookie.txt)" "https://adventofcode.com/{{year}}/day/${day}/input" > input
    code input
    code main.py

run day input="input":
    #!/usr/bin/env bash
    cd {{year}}/{{day}}
    (time poetry run python main.py < {{input}}) 2>&1 | tee output

lint day:
    poetry run black {{year}}/{{day}}/.
    poetry run flake8 {{year}}/{{day}}/.
