
import tkinter as tk


class TopLevelCentered(tk.Toplevel):
  def Init(self, name):
    self.title(name)

    # Get the screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    
    
    # Calculate the coordinates for the centered window
   
    w = 600
    h = 150
    window_width = w
    window_height = h
    x_coordinate = (screen_width - window_width) // 2
    y_coordinate = (screen_height - window_height) // 2

    # Set the geometry of the window to center it on the screen
    self.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
    return self
