import tkinter as tk
import subprocess
import threading

def execute_command():
    command = entry.get()  # Get the command from the entry widget
    input_data = input_entry.get().encode()  # Get the input data
    # Create a new thread to execute the command
    thread = threading.Thread(target=run_command, args=(command, input_data))
    thread.start()

def run_command(command, input_data):
    try:
        # Start the shell process and redirect the standard input/output/error
        shell_process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Send input data to the shell process
        output, error = shell_process.communicate(input=input_data)
        # Display the output and error messages
        window.after(0, update_output, output.decode())
        window.after(0, update_error, error.decode())
    except Exception as e:
        window.after(0, update_error, str(e))

def update_output(output):
    output_text.delete('1.0', tk.END)  # Clear the output text widget
    output_text.insert(tk.END, output)

def update_error(error):
    error_text.delete('1.0', tk.END)  # Clear the error text widget
    error_text.insert(tk.END, error)

# Create the main window
window = tk.Tk()
window.title("Command Line Shell Wrapper")

# Create an entry widget to input the shell command
entry = tk.Entry(window)
entry.pack()

# Create an entry widget to input the command data
input_entry = tk.Entry(window)
input_entry.pack()

# Create a button to execute the command
button = tk.Button(window, text="Execute", command=execute_command)
button.pack()

# Create a text widget to display the output
output_text = tk.Text(window)
output_text.pack()

# Create a text widget to display the error
error_text = tk.Text(window)
error_text.pack()

# Start the main event loop
window.mainloop()