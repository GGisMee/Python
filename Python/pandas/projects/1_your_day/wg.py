import tkinter as tk

# Create the root window
root = tk.Tk()

# Create the submission page frame
submission_frame = tk.Frame(root)

# Create the "submit" button
submit_button = tk.Button(submission_frame, text="Submit", command=lambda: show_new_screen(new_screen_frame))

# Add the button to the submission frame
submit_button.pack()

# Create the new screen frame and make it invisible
new_screen_frame = tk.Frame(root)
new_screen_frame.pack_forget()

# Create the widgets for the new screen frame
new_screen_label = tk.Label(new_screen_frame, text="This is the new screen!")

# Add the widgets to the new screen frame
new_screen_label.pack()

# Function to show the new screen
def show_new_screen(frame):
    # Remove the submission page frame
    submission_frame.pack_forget()
    # Show the new screen frame
    frame.pack()

# Add the submission page frame to the root window
submission_frame.pack()

# Start the main loop
root.mainloop()
