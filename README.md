# MSFS 2024 Livery Generator #

## what's the point ##
The point is to make it easier for sim enthusiasts to get liveries that they want, without necessarily having to learn everything about paintshop, the msfs livery tooling, and to break the process down into fewer, easier steps

## How to ##
### Setup ###
1. You will need to install GIMP v3 or later
1. You will need to grab a copy of the [https://github.com/theflaknine/ImageToMSFSKTX2][ImageToKTX2 tool] and put it in the same folder as the generate script files
Note the script expects to find a folder named ImageToMSFSKTX2-0.15 so if the version is different from this, please rename it or update the generator.py script. I will also do this occasionally in the repo.
1. you will need to setup the ImageToKtx2 tool by running it once initially.

### Setting up the cfg ###
There is a livery.cfg file here that is used to configure how you want the livery generated, basically next to each optional livery component, you put a colour. This can be a colour name like red, green or blue. Or it can be a HTML hash value like #ff0000, #00ff00 or #0000ff

You also get to chose the airframe, at the time of writing you could chose "arrow3" "warrior" or "tomahawk". you can see the full list of implemented features below.

You can chose between clean or dirty interior, this simply copies the correct ktx2 files to your chosen output folder

The folder name is the name...of the output folder where the finished files are sent, they are also sent into the ABDO folder of the ktx2 tool ready for you to run and convert.

Finally, the option for you to add a custom logo file. this should be a square logo, and whilst you can define the size (GIMP will scale you logo file for you) I would probably try it with default values to begin with.

### Run ### 
you can simply run either generateLivery file. `.bat` for windows and `.sh` for everywhere

