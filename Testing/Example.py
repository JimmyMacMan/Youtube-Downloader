import tkinter as tk
import subprocess
class TerminalApp:
   def __init__(self, root):
      self.root = root
      self.root.title("Listening to Terminal on Tkinter App")
      root.geometry("720x400")

      # Create a Text widget to display the terminal output
      self.output_text = tk.Text(self.root, wrap="word", height=20, width=50)
      self.output_text.pack(padx=10, pady=10)

      # Create a button to execute a command
      self.execute_button = tk.Button(self.root, text="Run Command", command=self.run_command)
      self.execute_button.pack(pady=10)

   def run_command(self):
      # The command you want to execute
      command = "help"

      # Use subprocess to run the command and capture the output
      result = subprocess.run(command, shell=True, capture_output=True, text=True)

      # Display the output in the Text widget
      self.output_text.delete("1.0", tk.END)  # Clear previous output
      self.output_text.insert(tk.END, result.stdout)
      self.output_text.insert(tk.END, result.stderr)

if __name__ == "__main__":
   root = tk.Tk()
   app = TerminalApp(root)
   root.mainloop()