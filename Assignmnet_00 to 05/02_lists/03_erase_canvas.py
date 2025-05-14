# tkinker library use for GUI applictaions(window, button or canvas etc.)
import tkinter as tk
# these are the constant taht use in program
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20
# function taht erase parts of the canvas and drag the mouse with the left button
def erase_objects(canvas, eraser):
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    
    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE
    
    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)
    # loop each overlapping and chnge the color to white
    for overlapping_object in overlapping_objects:
        canvas.itemconfig(overlapping_object, fill='white')

def main():
    root = tk.Tk()# is function se program start ho ga
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='lightblue')
    canvas.pack()# is function se ak naya window bane ga ya canvas
# calacution for rows and columns
    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE
# ye loop ak grid ready kare ga blue color ka means canvas jo banana hai.
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE
            
            cell = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill='blue')
# "create_rectangle" draws one cell at a time by calculating its position using row and column numbers.
    # update kre ga GUI ko takae wo mouse hilne se phle ready ho
    root.update()
    # Jab user mouse drag kare left button ke sath, tab erase_objects() function chalay aur canvas aur event pass ho jayein.
    canvas.bind('<B1-Motion>', lambda event: erase_objects(canvas, event))
    #                          anonymous function hai lambda
        # main loop run kre gay..
    root.mainloop()

if __name__ == '__main__':
    main()
