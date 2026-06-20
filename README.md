# MSFS 2024 Livery Generator

## What's the point

The point is to make it easier for sim enthusiasts to get liveries that they want, without necessarily having to learn everything about paintshop, the msfs livery tooling, and to break the process down into fewer, easier steps

## How to

### Setup

1. You will need to install [https://www.gimp.org/downloads/][GIMP v3 or later]
1. Download the [https://drive.google.com/drive/folders/1GR1gJhuDeFWz8hfg-Dw8R-S_bjVBlSZH?usp=sharing][gimp livery files] for the relevant aircraft. The are a copy of the PSD files, turned into XCF files and then updated with custom masks to enable the tool to automatically setup your livery. They are too big individually to be allowed in the free git teir I'm using
1. you will need to setup the ImageToKtx2 tool by running it once initially.
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

## Feature Completion

# Body

| Setting                   | Arrow 3 | Warrior | Tomahawk |
| ------------------------- | ------- | ------- | -------- |
| Base                      | - [ ]   | [x]     | - [ ]    |
| Belly                     | - [ ]   | [x]     | - [ ]    |
| High Tide Mark            | - [ ]   | [x]     | - [ ]    |
| Middle Tide Mark          | - [ ]   | [x]     | - [ ]    |
| Low Tide Mark             | - [ ]   | [x]     | - [ ]    |
| High Inverted Tide Mark   | - [ ]   | [x]     | - [ ]    |
| Middle Inverted Tide Mark | - [ ]   | [x]     | - [ ]    |
| Low Inverted Tide Mark    | - [ ]   | [x]     | - [ ]    |
| Swoosh                    | - [ ]   | [x]     | - [ ]    |
| Swoosh Line               | - [ ]   | [x]     | - [ ]    |
| Cheat Line 1              | - [ ]   | [x]     | - [ ]    |
| Cheat Line 2              | - [ ]   | [x]     | - [ ]    |
| Cheat Line 3              | - [ ]   | [x]     | - [ ]    |
| Cheat Line 4              | - [ ]   | [x]     | - [ ]    |
| Cheat Line 5              | - [ ]   | [x]     | - [ ]    |
| Arrow 1                   | - [ ]   | [x]     | - [ ]    |
| Arrow 2                   | - [ ]   | [x]     | - [ ]    |
| Arrow 3                   | - [ ]   | [x]     | - [ ]    |
| Hockey Stick 1            | - [ ]   | - [ ]   | - [ ]    |
| Hockey Stick 2            | - [ ]   | - [ ]   | - [ ]    |

# Tail

| Setting                   | Arrow 3 | Warrior | Tomahawk |
| ------------------------- | ------- | ------- | -------- |
| Base                      | - [ ]   | [x]     | - [ ]    |
| Arrow 1                   | - [ ]   | - [ ]   | - [ ]    |
| Arrow 2                   | - [ ]   | - [ ]   | - [ ]    |
| Arrow 3                   | - [ ]   | - [ ]   | - [ ]    |
| High Tide Mark            | - [ ]   | - [ ]   | - [ ]    |
| Middle Tide Mark          | - [ ]   | - [ ]   | - [ ]    |
| Low Tide Mark             | - [ ]   | - [ ]   | - [ ]    |
| High Inverted Tide Mark   | - [ ]   | - [ ]   | - [ ]    |
| Middle Inverted Tide Mark | - [ ]   | - [ ]   | - [ ]    |
| Low Inverted Tide Mark    | - [ ]   | - [ ]   | - [ ]    |
| Logo Image                | - [ ]   | [x]     | - [ ]    |
| Logo Size                 | - [ ]   | [x]     | - [ ]    |

# Wing

| Setting                   | Arrow 3 | Warrior | Tomahawk |
| ------------------------- | ------- | ------- | -------- |
| Base                      | - [ ]   | [x]     | - [ ]    |
| Belly                     | - [ ]   | [x]     | - [ ]    |
| High Tide Mark            | - [ ]   | - [ ]   | - [ ]    |
| Middle Tide Mark          | - [ ]   | - [ ]   | - [ ]    |
| Low Tide Mark             | - [ ]   | - [ ]   | - [ ]    |
| High Inverted Tide Mark   | - [ ]   | - [ ]   | - [ ]    |
| Middle Inverted Tide Mark | - [ ]   | - [ ]   | - [ ]    |
| Low Inverted Tide Mark    | - [ ]   | - [ ]   | - [ ]    |
