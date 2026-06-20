# MSFS 2024 Livery Generator

## Table of Contents

- [MSFS 2024 Livery Generator](#msfs-2024-livery-generator)
  - [What's the Point](#whats-the-point)
  - [How to](#how-to)
    - [Setup](#setup)
    - [Setting up the CFG](#setting-up-the-cfg)
    - [Run](#run)
  - [Feature Completion](#feature-completion)
    - [Body](#body)
    - [Tail](#tail)
    - [Wing](#wing)
  - [How Can I Help](#how-can-i-help)

## What's the point

The point is to make it easier for sim enthusiasts to get liveries that they want, without necessarily having to learn everything about paintshop, the msfs livery tooling, and to break the process down into fewer, easier steps

## How to

### Setup

1. You will need to install [GIMP v3 or later](https://www.gimp.org/downloads/)
1. Download the [gimp livery files](https://drive.google.com/drive/folders/1GR1gJhuDeFWz8hfg-Dw8R-S_bjVBlSZH?usp=sharing) for the relevant aircraft. The are a copy of the PSD files, turned into XCF files and then updated with custom masks to enable the tool to automatically setup your livery. They are too big individually to be allowed in the free git teir I'm using
1. you will need to setup the ImageToKtx2 tool by running it once initially. [KTX2 image tool here](https://github.com/theflaknine/ImageToMSFSKTX2/releases)
1. Set up the config file `livery.cfg`

### Setting up the cfg

There is a livery.cfg file here that is used to configure how you want the livery generated, basically next to each optional livery component, you put a colour. This can be a colour name like red, green or blue. Or it can be a HTML hash value like #ff0000, #00ff00 or #0000ff

You also get to chose the airframe, at the time of writing you could chose "arrow3" "warrior" or "tomahawk". you can see the full list of implemented features below.

You can chose between clean or dirty interior, this simply copies the correct ktx2 files to your chosen output folder

The folder name is the name...of the output folder where the finished files are sent, they are also sent into the ABDO folder of the ktx2 tool ready for you to run and convert.

Finally, the option for you to add a custom logo file. this should be a square logo, and whilst you can define the size (GIMP will scale you logo file for you) I would probably try it with default values to begin with.

### Run

1. you can simply run either generateLivery file. `.bat` for windows and `.sh` for everywhere
1. The files will be put in the folder name you chose (or customlivery by default)
1. You can check the PNG file to see if it looks about right, and the XCF files if you want to futher modify the livery, then export as PNG again.
1. Then you can run the `Image to MSFS KTX2.bat` in the image2ktx folder to generate the correct output files for the compiled livery
1. Finally copy that into the correct part of your community folder. I recommend using a working example from flightsim.to and then replacing the files in the folder with the ones you generated, update the cfg files in that folder to use your name etc.

## Feature Completion

### TODO

- [ ] finish masking warrior
- [ ] Mask arrow3
- [ ] Mask tomahawk
- [ ] Work out how to make white dynamic rego for liveries (at least document the porocess for the community)
- [ ] Chose next airframe(s) to mask

### Body

| Setting                   | Arrow 3      | Warrior            | Tomahawk     |
| ------------------------- | ------------ | ------------------ | ------------ |
| Base                      | :red_square: | :white_check_mark: | :red_square: |
| Belly                     | :red_square: | :white_check_mark: | :red_square: |
| High Tide Mark            | :red_square: | :white_check_mark: | :red_square: |
| Middle Tide Mark          | :red_square: | :white_check_mark: | :red_square: |
| Low Tide Mark             | :red_square: | :white_check_mark: | :red_square: |
| High Inverted Tide Mark   | :red_square: | :white_check_mark: | :red_square: |
| Middle Inverted Tide Mark | :red_square: | :white_check_mark: | :red_square: |
| Low Inverted Tide Mark    | :red_square: | :white_check_mark: | :red_square: |
| Swoosh                    | :red_square: | :white_check_mark: | :red_square: |
| Swoosh Line               | :red_square: | :white_check_mark: | :red_square: |
| Cheat Line 1              | :red_square: | :white_check_mark: | :red_square: |
| Cheat Line 2              | :red_square: | :white_check_mark: | :red_square: |
| Cheat Line 3              | :red_square: | :white_check_mark: | :red_square: |
| Cheat Line 4              | :red_square: | :white_check_mark: | :red_square: |
| Cheat Line 5              | :red_square: | :white_check_mark: | :red_square: |
| Arrow 1                   | :red_square: | :white_check_mark: | :red_square: |
| Arrow 2                   | :red_square: | :white_check_mark: | :red_square: |
| Arrow 3                   | :red_square: | :white_check_mark: | :red_square: |
| Hockey Stick 1            | :red_square: | :red_square:       | :red_square: |
| Hockey Stick 2            | :red_square: | :red_square:       | :red_square: |

### Tail

| Setting                   | Arrow 3      | Warrior            | Tomahawk     |
| ------------------------- | ------------ | ------------------ | ------------ |
| Base                      | :red_square: | :white_check_mark: | :red_square: |
| Arrow 1                   | :red_square: | :red_square:       | :red_square: |
| Arrow 2                   | :red_square: | :red_square:       | :red_square: |
| Arrow 3                   | :red_square: | :red_square:       | :red_square: |
| High Tide Mark            | :red_square: | :red_square:       | :red_square: |
| Middle Tide Mark          | :red_square: | :red_square:       | :red_square: |
| Low Tide Mark             | :red_square: | :red_square:       | :red_square: |
| High Inverted Tide Mark   | :red_square: | :red_square:       | :red_square: |
| Middle Inverted Tide Mark | :red_square: | :red_square:       | :red_square: |
| Low Inverted Tide Mark    | :red_square: | :red_square:       | :red_square: |
| Logo Image                | :red_square: | :white_check_mark: | :red_square: |
| Logo Size                 | :red_square: | :white_check_mark: | :red_square: |

### Wing

| Setting                   | Arrow 3      | Warrior            | Tomahawk     |
| ------------------------- | ------------ | ------------------ | ------------ |
| Base                      | :red_square: | :white_check_mark: | :red_square: |
| Belly                     | :red_square: | :white_check_mark: | :red_square: |
| High Tide Mark            | :red_square: | :red_square:       | :red_square: |
| Middle Tide Mark          | :red_square: | :red_square:       | :red_square: |
| Low Tide Mark             | :red_square: | :red_square:       | :red_square: |
| High Inverted Tide Mark   | :red_square: | :red_square:       | :red_square: |
| Middle Inverted Tide Mark | :red_square: | :red_square:       | :red_square: |
| Low Inverted Tide Mark    | :red_square: | :red_square:       | :red_square: |

## How can I help

I need people to provide more livery files! The requirements are kinda simple, gimp xcf files with the layers setup the same as my examples (Currently the warrior is mostly ready).
I also haven't actually got a Tomahawk or Arrow3 to test the generated liveries on, so I need someone to do that too!
