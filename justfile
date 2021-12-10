year := "2021"

_:
    @just -l -u --list-heading $'Welcome to {{year}} AoC 🎄\n'

# Python

start day:
    #!/usr/bin/env bash
    cd {{year}}
    mkdir -p {{day}}
    cd {{day}}
    touch main.py
    day=$((10#{{day}}))
    # echo "session=53616c74..." > cookie.txt
    url="https://adventofcode.com/{{year}}/day/${day}"
    curl -b "$(cat {{justfile_directory()}}/cookie.txt)" "${url}/input" > input
    echo $url
    just sample "${url}" > sample
    code input
    code sample
    code main.py

sample url:
    #!.venv/bin/python
    import requests
    from bs4 import BeautifulSoup
    page = requests.get("{{url}}").text.encode('utf-8')
    soup = BeautifulSoup(page, "html.parser")
    print(soup.find('pre').find('code').contents[0].strip())

run day input="input":
    #!/usr/bin/env bash
    cd {{year}}/{{day}}
    (time poetry run python main.py < {{input}}) 2>&1 | tee output

lint day:
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
