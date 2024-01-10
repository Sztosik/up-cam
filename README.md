# Martian Mines

Competition code for Martian Mines for Droniad 2024 competition.

## Instalation

### Install required package

*Manjaro:*

```bash
$ sudo pamac install gphoto2
```

*Fedora:*

```bash
$ sudo dnf install gphoto2
```

*RaspberyPi:*

```bash
$ sudo apt install gphoto2
```

### Setup repository

```bash
$ git clone git@gitlab.com:academic-aviation-club/droniada-2024/martian-mines.git
$ cd martian-mines
$ poetry install --no-root
$ poetry shell
```

### Setup repository on RaspberyPi:

```bash
$ git clone git@gitlab.com:academic-aviation-club/droniada-2024/martian-mines.git
$ cd martian-mines
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### Hardware preparation

1. Connect camera to the on-board computer,
2. Set the 2-position switch on RC channel 8,

> Note, PWM signal > `1500` ms on the 8th RC channel activates the script.

### Run production code

```bash
$ python -m martian_mines
```

### SITL testing

```bash
$ python -m martian-mines -S -N
```

### Run example

```bash
$ python -m examples.state_machine_example
```

## Instruction for Windows users

Read this [installation guide](https://docs.fedoraproject.org/en-US/fedora/latest/getting-started/)