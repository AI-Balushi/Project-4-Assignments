import tkinter as tk

# Constants for canvas and grid settings
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

CELL_SIZE = 40  # Size of each grid cell
ERASER_SIZE = 20  # Size of the eraser

def erase_objects(canvas, eraser, event):
    """Erase objects in contact with the eraser"""
    # Get the mouse coordinates
    mouse_x = event.x
    mouse_y = event.y
    
    # Calculate the position of the eraser
    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE
    
    # Find overlapping objects with the eraser
    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)
    
    # For everything that overlaps with the eraser, change its color to white
    for overlapping_object in overlapping_objects:
        canvas.itemconfig(overlapping_object, fill='white')

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Eraser on Canvas")

    # Create the canvas
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()

    # Create a grid of blue cells
    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE
    
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE
            
            # Create a blue rectangle for each cell
            canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill='blue')

    # Create the eraser as a pink rectangle
    eraser = canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill='pink')

    # Bind the mouse motion to move the eraser and erase cells
    canvas.bind("<Motion>", lambda event: erase_objects(canvas, eraser, event))

    # Start the Tkinter main loop
    root.mainloop()

if __name__ == '__main__':
    main()
