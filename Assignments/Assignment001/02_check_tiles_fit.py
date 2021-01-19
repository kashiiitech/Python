"""function with the name “checkTilesFit” which takes in four inputs
(plot_width, plot_length, tile_width, tile_length) and checks the tiles with the
length and width given in the parameter fit into the area of the plot, If yes then
this function return “True” else this function return “False”."""





def checkTilesFit(plot_width,plot_length,tile_width,tile_length):
    plot_area = plot_width*plot_length
    tile_area = tile_width*tile_length
    if plot_width < 0 or plot_length<0 or tile_width<0 or tile_length<0:
        return False
    elif plot_area%tile_area==0 and (plot_width%tile_width==0) and (plot_length%tile_length==0):
        return True
    elif plot_width%tile_length==0 and plot_length%tile_width==0:
        return True
    else:
        return False
