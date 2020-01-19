# Griznog

[![PyPI version](https://badge.fury.io/py/griznog.svg)](https://pypi.org/project/griznog)
[![GitHub actions status](https://github.com/vsoch/griznog/workflows/ci/badge.svg?branch=master)](https://github.com/vsoch/griznog/actions?query=branch%3Amaster+workflow%3Aci)

[![asciicast](https://asciinema.org/a/294628.svg)](https://asciinema.org/a/294628)

## Usage

> I'm a redneck, I never read the instructions.
> --Griznog 4/26/2019

Well, there are still several use cases you might want to read about!

 - [Install](#install)
 - [Command Line Usage](#command-line-usage)
 - [Python Usage](#python-usage)
 - [Container Usage](#container-usage)


### Install

Install your Griznog from pypi

```bash
pip install griznog
```

or install from the repository directly:

```bash
$ git clone https://github.com/vsoch/griznog
$ cd griznog
$ python setup.py install
```

### Command Line Usage

The main utility of Griznog is to speak:

```bash
$ griznog --help
usage: griznog [-h] [--version] {speak} ...

Griznog, captured in code

optional arguments:
  -h, --help  show this help message and exit
  --version   print the version and exit.

actions:
  actions for Griznog

  {speak}     griznog actions
    speak     ask Griznog to speak his wisdom.
```

and specifically, we can ask for a random quote (no arguments), filter to a 
topic (`--topic <topic>`), disable color, or have him dump all of his wisdom 
(with some pause between quotes).

```bash
$ griznog speak --help

usage: griznog speak [-h] [--topic TOPIC] [--pause PAUSE] [--dump]
                     [--no-color]

optional arguments:
  -h, --help     show this help message and exit
  --topic TOPIC  subset to particular topic.
  --pause PAUSE  seconds to allow Griznog to breathe between spurts (default 3
                 seconds).
  --dump         Just hear everything. Optionally set a --pause (seconds)
  --no-color     disable color
```

#### 1. Random Quote

```bash
$ griznog speak

griznog hopes everyone has an anxiety attack and leaves him alone with 10 pizzas.

--Griznog 11/28/2018
```

### 2. Quote filtered to topic

```bash
$ griznog speak --topic pizza

We are fairly simple creatures, throw us the occasional beer, donut and pizza, send us hardware (in quantities that are powers of 2!) and lock us in the basement and we are happy.

--Griznog 8/31/2018
```


### 3. Quote Dump

```bash
$ griznog speak --dump
```

Disable color (also works for previously mentioned commands)

```bash
$ griznog speak --dump --no-color
```


### Python Usage

#### 1. Create your Griznog

First, create your Griznog.

```python
from griznog import Griznog
> human = Griznog()
```

#### 2. Wisdom

Ask your Griznog for a random point of wisdom!

```python
> human.speak()
The sad reality is that the universe doesn't work this way. In the same way we carry DNA and RNA that is billions of years old, we are stuck with legacy code. Organisms aren't rewarded by evolution for making giant rewrites, and programmers aren't rewarded by HR for making things simpler or starting over fresh.

--Griznog 10/11/2018
```

Optionally you can filter to a particular topic.

```python
> human.speak(topic='container')

I said they were surprisingly powerful, I didn't mean container fanbois couldn't screw them up.

--Griznog 9/13/2018
```

For an entertaining stream of wisdom, you know what to do:

```python
> human.dump()
```

You can also dump with a filtered set:

```python
> human.dump(topic='container')
```

For any of the above, if your terminal doesn't support color, just disable it.

```python
> human.speak(add_color=False)
```

### Container Usage

Griznog is... trapped in a container!

```bash
docker run -it quay.io/vanessa/griznog speak

job security. I get scared when any of this works too well.

--Griznog 4/12/2018
```

Do you have a question? Or want to suggest a feature to make it better?
Please [open an issue!](https://www.github.com/vsoch/griznog/issues)
