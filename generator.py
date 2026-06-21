# Standard python-fu imports
from pathlib import Path
import shutil
import gi
gi.require_version('Gimp', '3.0')
from gi.repository import Gimp
import configparser

pdb = Gimp.get_pdb()
customLiveryLayerName = 'Custom'
liveriesLayerName='Liveries'

def main():
    config = configparser.ConfigParser()
    config.read("./livery.cfg")
    
    livery_name=config.get("Files","folder_name")
    airframe=config.get("Files","airframe")
    cleanInterior=config.get("Files","clean")
    folder_path=None
    match airframe:
        case "warrior":
            folder_path=Path('PA-28-Warrior')
        case "arrow3":
            folder_path=Path('PA-28-Arrow3')
        case "tomahawk":
            folder_path=Path('PA-38-Tomahawk')
    output_path=Path(livery_name)
    output_path.mkdir(exist_ok=True)
    for base_template_file in folder_path.iterdir():
        if not base_template_file.suffix == '.xcf':
            continue
        cleanName = base_template_file.name.removesuffix(base_template_file.suffix)
        # 1. Access the GIMP Procedure Database (PDB)

        # 2. Load the main target XCF file
        # In GIMP 3, file handling uses Gio.File objects
        print(f"Processing: {folder_path.name}/{base_template_file.name}")

        xcf_file = Gio.File.new_for_path(folder_path.name+'/'+base_template_file.name)
        image = Gimp.file_load(Gimp.RunMode.NONINTERACTIVE, xcf_file)
        if not image:
            print("Error: Could not load the XCF file.")
            return
   
        # 3. Find the old target layer by its name
        liveries = image.get_layer_by_name(liveriesLayerName)
        if not liveries:
            print("No liveries layer found, skipping file")
            save(image, output_path, base_template_file, cleanName)
            continue
        custom = None
        # printLayer(liveries)
        for child in liveries.get_children():
            # print('livery children '+child.get_name()) 
            if child.get_name() == customLiveryLayerName:
                custom = child
        if not custom:
            print("No custom layer found, skipping file")
            save(image, output_path, base_template_file, cleanName)
            continue
        for sectionLayer in custom.get_children():
            sectionLiveryLayer = LiveryLayerSection(sectionLayer, config)
            for maskLayer in sectionLayer.get_children():
                sectionLiveryLayer.mapLayer(image,maskLayer)
           
        # print("=== IMAGE TREE ===")
        # for layer in image.get_layers():
        #     dump(layer)
        save(image, output_path, base_template_file, cleanName)
        print("Next file")
    if cleanInterior:
        print("Clean Interior chosen")
        shutil.copytree(Path(folder_path.name+"/Clean/"),output_path,dirs_exist_ok=True)
    else:
        print("Default Interior chosen")
        shutil.copytree(Path(folder_path.name+"/Default/"),output_path,dirs_exist_ok=True)
    print("Success: Your custom livery has been generated and saved.")

def save(image, output_path, base_template_file, cleanName):
    
    print(f"saving {base_template_file.name} and {cleanName}.png files")
    out_xcf = Gio.File.new_for_path(output_path.name+"/"+base_template_file.name)
    out_png = Gio.File.new_for_path(output_path.name+"/"+cleanName+'.png')
    # print('xcf')
    Gimp.file_save(Gimp.RunMode.NONINTERACTIVE, image, out_xcf)
    # print('png')
    Gimp.file_save(Gimp.RunMode.NONINTERACTIVE, image, out_png)

    ktx2gen = Gio.File.new_for_path("./ImageToMSFSKTX2-0.15/ALBD/"+cleanName+'.png')
    # print('KTX2 png')
    Gimp.file_save(Gimp.RunMode.NONINTERACTIVE, image, ktx2gen)

    # Clean up image memory
    image.delete()

def dump(item, depth=0):
    print("  " * depth + item.get_name())

    try:
        for child in item.get_children():
            dump(child, depth + 1)
    except:
        pass



class LiveryLayerSection:

    def __init__(self, section, config):
        self.section_name = section.get_name()
        print(f"setting up {self.section_name}")
        # Mapping config lines to object fields
        self.layer_map = {
            "Base "+self.section_name:config.get(self.section_name, 'base', fallback=None),
            "Belly "+self.section_name:config.get(self.section_name, "belly",  fallback=None),
            "HighTide "+self.section_name:config.get(self.section_name, "high_tide_mark",  fallback=None),
            "MiddleTide "+self.section_name:config.get(self.section_name, "middle_tide_mark",  fallback=None),
            "LowTide "+self.section_name:config.get(self.section_name, "low_tide_mark",  fallback=None),
            
            "InvertedHighTide "+self.section_name:config.get(self.section_name, "high_inverted_tide_mark",  fallback=None),
            "InvertedMiddleTide "+self.section_name:config.get(self.section_name, "middle_inverted_tide_mark",  fallback=None),
            "InvertedLowTide "+self.section_name:config.get(self.section_name, "low_inverted_tide_mark",  fallback=None),
            
            "Swoosh "+self.section_name:config.get(self.section_name, "swoosh",  fallback=None),
            "SwooshLine "+self.section_name:config.get(self.section_name, "swoosh_line",  fallback=None),
            
            "Cheat1 "+self.section_name:config.get(self.section_name, "cheat_line_1",  fallback=None),
            "Cheat2 "+self.section_name:config.get(self.section_name, "cheat_line_2",  fallback=None),
            "Cheat3 "+self.section_name:config.get(self.section_name, "cheat_line_3",  fallback=None),
            "Cheat4 "+self.section_name:config.get(self.section_name, "cheat_line_4",  fallback=None),
            "Cheat5 "+self.section_name:config.get(self.section_name, "cheat_line_5",  fallback=None),
            
            "Arrow1 "+self.section_name:config.get(self.section_name, "arrow_1",  fallback=None),
            "Arrow2 "+self.section_name:config.get(self.section_name, "arrow_2",  fallback=None),
            "Arrow3 "+self.section_name:config.get(self.section_name, "arrow_3",  fallback=None),
            
            "HockeyStick1 "+self.section_name:config.get(self.section_name, "hockey_stick_1",  fallback=None),
            "HockeyStick2"+self.section_name:config.get(self.section_name, "hockey_stick_2",  fallback=None),
        }
        
        self.logo_size=config.getint(self.section_name, "logo_size",  fallback=None)
        self.logo_image=config.get(self.section_name, "logo_image",  fallback=None)
        self.logo_flip=config.getboolean(self.section_name, "logo_flip",  fallback=None)

    def mapLayer(self ,image, layer):
        # print(f"Checking if mask {layer.get_name()} should be used")
        if 'Logo' in layer.get_name() and self.logo_image:
            self._setLogo(image, layer)
        elif layer.get_name() in self.layer_map and self.layer_map[layer.get_name()]:
            self._setMaskcolour(layer, self.layer_map[layer.get_name()]) 
        # else:
        #     print("No setting found, moving on")

    def _setMaskcolour(self, layer, colour):
        print(f"mask {layer.get_name()} will be {self.layer_map[layer.get_name()]}")
        gcolour = Gegl.Color.new(colour)
        Gimp.context_set_background(gcolour) 
        layer.fill(Gimp.FillType.BACKGROUND)

    def _setLogo(self, image, layer):
        image_location =self.logo_image
        image_size=self.logo_size
        should_flip=self.logo_flip
        layername = layer.get_name()
        width = layer.get_width()
        height = layer.get_height()

        print(f"putting logo {image_location} on {layer.get_name()}")
        # 4. Load the replacement image as a new standalone layer object
        new_logo_file = Gio.File.new_for_path(image_location)
        # print(f"new_logo_file is {new_logo_file}")
        # Using the PDB procedure to load an external file directly as a layer
        newLogoLayer1 = Gimp.file_load_layer(Gimp.RunMode.NONINTERACTIVE, image, new_logo_file)

        if not newLogoLayer1 :
            print("Error: Failed to load replacement image as a layer.")
            return
        
        # 5. Capture the geometry metadata from the old layer
        position1 = image.get_item_position(layer) # Stack position
        parent1 = layer.get_parent()              # Check if it lives inside a layer group
        success1, x_offset1, y_offset1 = layer.get_offsets() # Keep original placement
        
        image.insert_layer(newLogoLayer1, parent1, position1)        
        
        newLogoLayer1.set_name(layername) # Take over the old layer name        
        newLogoLayer1.scale(image_size,image_size,0)
        newLogoLayer1.set_offsets(x_offset1, y_offset1)
        image.remove_layer(layer)
        # 6. Insert the new layer and match coordinates
        if should_flip and '2' in layername:
            flipped = newLogoLayer1.transform_flip_simple(
                Gimp.OrientationType.HORIZONTAL,
                True,
                0
            )            

            newLogoLayer1 = flipped
            newLogoLayer1.set_name(layername) # Take over the old layer name        
            newLogoLayer1.set_offsets(x_offset1, y_offset1)

        
        



