deep_water = "#0000CD"
water = "#1E90FF"
desert = "#cdb380"
lifeless = "#e8ddcb"
tundra = "#fffbf0"
mountain = "#666460"

coolwet = "#228B22"
warmwet = "#006400"
cooldry = "#8FBC8F"
warmdry = "#808000"
warm = "#008000"
cool = "#32CD32"

def color_variant(hex_color, brightness_offset=1):
    """ takes a color like #87c95f and produces a lighter or darker variant """
    if len(hex_color) != 7:
        raise Exception("Passed %s into color_variant(), needs to be in #87c95f format." % hex_color)
    rgb_hex = [hex_color[x:x+2] for x in [1, 3, 5]]
    new_rgb_int = [int(hex_value, 16) + brightness_offset for hex_value in rgb_hex]
    new_rgb_int = [min([255, max([0, i])]) for i in new_rgb_int] # make sure new values are between 0 and 255
    # hex() produces "0x88", we want just "88"
    return "#" + "".join([hex(i)[2:] for i in new_rgb_int])

def getColour(height, moisture = 100):
    if(height < 25):
        return deep_water
    if(height < 100):
        return water
    if(height < 150):
        if(moisture < 70):
            return color_variant(desert,int(height-180))
        elif(moisture < 115):
            return warm
        elif(moisture < 160):
            return warmwet
    if(height < 200):
        if(moisture < 70):
            return color_variant(tundra,int(height-180))
        elif(moisture < 115):
            return cool
        elif(moisture < 160):
            return coolwet
    return color_variant(mountain,int(height-180))

def getGreyScale(height):
    h = int(max(0, min(height, 255)))
    return '#%02x%02x%02x' % (h, h, h)
def hexToTriple(hexString):
    return (int(hexString[1:3],16), int(hexString[3:5],16), int(hexString[5:7],16) )
