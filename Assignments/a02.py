### YOUR CODE FOR calculateArea() FUNCTION GOES HERE ###
def calculateArea(length,width):
    area=length*width
    return area      
#### End OF MARKER



### YOUR CODE FOR checkTilesFit() FUNCTION GOES HERE ###
def checkTilesFit(plot_length,plot_width,tile_length,tile_width):
    plot_area = plot_length*tile_length
    tile_area = tile_length*tile_width
    if plot_area%tile_area == 0 and (plot_length%tile_length == 0 or plot_length%tile_length==0) and (plot_width%tile_width == 0 or plot_width%tile_length):
        return True
    else:
        return False	
    
#### End OF MARKER



### YOUR CODE FOR calculateTiles() FUNCTION GOES HERE ###
def calculateTiles(plot_width,plot_length,tile_width,tile_length):
    if type(plot_width)==str or type (plot_length) == str or type (tile_width) == str or type(tile_length) == str:
        return "Invalid Input"
    if plot_width == 0 or plot_length == 0 or tile_width == 0 or tile_length == 0 or (plot_width,plot_length,tile_width,tile_length) == 0:
        return None
    
    plot_area = plot_width*plot_length
    tile_area = tile_width*tile_length
    number_of_tiles= plot_area//tile_area
    if plot_area%tile_area == 0:
        return number_of_tiles
    else:
        return "Not Possible"
    return plot_area//tile_area
#### End OF MARKER



