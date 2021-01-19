""" function with the name “calculateTiles” that takes in four inputs
(plot_width, plot_length, tile_wdith, tile_length) and returns the number of tiles
required to cover the whole plot without breaking the tiles. The number of tiles
should be an integer not a float. """

# Conditions

#  a. If the type of any of the parameters is “str”, return “Invalid Input”.

# b. If the value of any of the parameters is zero, return None.

""" c. You have to call the “checkTilesFit” function, If this “checkTilesFit” function
returns “True” then you need to return the number of tiles after calculating
the number of tiles else you have to return “Not Possible”."""




def calculateTiles(plot_width,plot_length,tile_width,tile_length):
    plot_area = plot_width*plot_length
    tile_area = tile_width*tile_length
    if type(plot_width) == str or type(plot_length) == str or type(tile_width) == str or type(tile_length) == str:
        return "Invalid Input"
    elif plot_width == 0 or plot_length == 0 or tile_width == 0 or tile_length == 0:
        return print(None)
    elif checkTilesFit(plot_width, plot_length, tile_width, tile_length) == True:
        plot_area = calculateArea(plot_width, plot_length)
        tiles_area = calculateArea(tile_width, tile_length)
        return plot_area // tile_area
    
    else:
        return "Not Possible"

