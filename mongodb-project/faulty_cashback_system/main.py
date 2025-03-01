# Faulty Cashback System

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  # For handling and displaying images
import pymongo
import random
import datetime

class FaultyCashbackSystem:
    def __init__(self, root):
        # Initialize main window properties
        self.root = root
        self.root.title("Faulty Cashback System")
        self.root.geometry("500x400")  # Set window size
        self.root.maxsize(500, 400)     # Set maximum window size
        self.root.configure(bg="#34495e")  # Background color
        
        # Connect to MongoDB database and get collections
        self.client = pymongo.MongoClient("LINK")
        self.db = self.client["FaultyCashbackSystem"]
        self.collection = self.db["FaultyCashbackSystem"]
        self.rewards = self.db["Rewards"]  # New collection to store rewards
        
        self.add_logo()           # Display logo in top left corner
        self.show_initial_screen()  # Show the initial screen

    def add_logo(self):
        # Load and display the logo from assets folder
        logo_image = Image.open("assets/logoCJ.png")
        logo_image = logo_image.resize((50, 50), Image.LANCZOS)  # Resize with high-quality filter
        self.logo = ImageTk.PhotoImage(logo_image)
        # Place logo at coordinates (10,10)
        self.logo_label = Label(self.root, image=self.logo, bg="#34495e")
        self.logo_label.place(x=10, y=10)

    def show_initial_screen(self):
        # Create a frame for the initial screen with fixed width and height
        self.initial_frame = Frame(self.root, bg="#34495e", width=400, height=300)
        # Center the frame on the window
        self.initial_frame.place(relx=0.5, rely=0.4, anchor=CENTER)
        
        # Add a label with the initial question
        self.initial_label = Label(self.initial_frame, text="Do you want to proceed with the payment?", 
                                     bg="#34495e", fg="#ecf0f1", font=("Helvetica", 16, "bold"))
        self.initial_label.pack(pady=20)
        
        # "Yes" button to proceed to payment screen
        self.yes_button = Button(self.initial_frame, text="Yes", command=self.create_widgets, 
                                 bg="#2ecc71", fg="white", font=("Helvetica", 12, "bold"),
                                 relief=FLAT, bd=5, padx=15, pady=8)
        self.yes_button.pack(pady=10)
        
        # "No" button to quit the application
        self.no_button = Button(self.initial_frame, text="No", command=self.root.quit, 
                                bg="#e74c3c", fg="white", font=("Helvetica", 12, "bold"),
                                relief=FLAT, bd=5, padx=15, pady=8)
        self.no_button.pack(pady=10)

    def create_widgets(self):
        # Hide the initial screen frame
        self.initial_frame.place_forget()
        
        # Create payment screen frame with same size as initial screen
        self.payment_frame = Frame(self.root, bg="#34495e", width=400, height=300)
        self.payment_frame.place(relx=0.5, rely=0.4, anchor=CENTER)
        
        # Label prompting the user to enter the payment amount
        self.payment_amount_label = Label(self.payment_frame, text="Enter the payment amount", 
                                          bg="#34495e", fg="#ecf0f1", font=("Helvetica", 16, "bold"))
        self.payment_amount_label.pack(pady=20)
        
        # Entry widget for the payment amount
        self.payment_amount_entry = Entry(self.payment_frame, font=("Helvetica", 14), relief=SOLID, bd=2)
        self.payment_amount_entry.pack(pady=10)
        
        # Label for error messages; initially empty
        self.error_label = Label(self.payment_frame, text="", fg="white", bg="#34495e", font=("Helvetica", 10))
        self.error_label.pack()
        
        # "Payment" button to initiate the payment process
        self.payment_button = Button(self.payment_frame, text="Payment", command=self.payment, 
                                     bg="#3498db", fg="white", font=("Helvetica", 12, "bold"),
                                     relief=FLAT, bd=5, padx=15, pady=8)
        self.payment_button.pack(pady=10)
        # "Back" button remains unchanged
        self.back_button = Button(self.payment_frame, text="Back", command=self.back_to_initial, 
                                  bg="#95a5a6", fg="white", font=("Helvetica", 12, "bold"),
                                  relief=FLAT, bd=5, padx=15, pady=8)
        self.back_button.pack(pady=5)
        
    def back_to_initial(self):
        # Hide the payment frame and show the initial screen again
        self.payment_frame.place_forget()
        self.show_initial_screen()

    def payment(self):
        # Retrieve and validate the payment amount and convert it into an integer value
        payment_amount = self.payment_amount_entry.get()
        try:
            int_value = int(payment_amount)
        except ValueError:
            self.error_label.config(text="Input is not accepted! Please enter an integer value.")
            return
        if int_value == 0:
            self.error_label.config(text="Please enter the payment amount!")
            return
        self.error_label.config(text="")  # Clear error if valid
        
        # Store payment details in MongoDB and save the inserted id
        data = {
            "payment_amount": int_value,
            "payment_date": datetime.datetime.now()
        }
        result = self.collection.insert_one(data)
        self.last_payment_id = result.inserted_id  # Save payment id for later update
        self.show_message("Payment", "Payment done successfully", self.faulty_cashback_system)
    
    def faulty_cashback_system(self):
        # Randomly determine reward outcome
        random_number = random.randint(1, 100)
        
        if random_number <= 80:  # 80% chance for a coupon
            coupon = f"Coupon{random.randint(1, 100)}"
            reward_record = {
                "reward_type": "Coupon",
                "reward_detail": coupon,
                "reward_date": datetime.datetime.now()
            }
            try:
                # Insert reward record in Rewards collection
                result = self.rewards.insert_one(reward_record)
            except Exception as e:
                self.show_message("Error", "Some error occurred while inserting reward")
            # Update the payment record with reward info
            self.collection.update_one({"_id": self.last_payment_id}, {"$set": {"reward": reward_record}})
            self.show_message("Coupon", f"Congratulations! You have won a coupon: {coupon}")
        elif random_number <= 95:  # 15% chance for "Better Luck Next Time"
            reward_record = {
                "reward_type": "Better Luck",
                "reward_detail": "BETTER LUCK NEXT TIME",
                "reward_date": datetime.datetime.now()
            }
            try:
                result = self.rewards.insert_one(reward_record)
            except Exception as e:
                self.show_message("Error", "Some error occurred while inserting reward")
            self.collection.update_one({"_id": self.last_payment_id}, {"$set": {"reward": reward_record}})
            self.show_message("Better Luck Next Time", "BETTER LUCK NEXT TIME")
        else:  # 5% chance for cashback
            cashback = random.randint(1, 100)
            reward_record = {
                "reward_type": "Cashback",
                "reward_detail": cashback,
                "reward_date": datetime.datetime.now()
            }
            try:
                result = self.rewards.insert_one(reward_record)
            except Exception as e:
                self.show_message("Error", "Some error occurred while inserting reward")
            self.collection.update_one({"_id": self.last_payment_id}, {"$set": {"reward": reward_record}})
            self.show_message("Cashback", f"Congratulations! You have won {cashback} cashback")
    
    def show_message(self, title, message, callback=None):
        # Create a custom message box as a top-level window
        top = Toplevel(self.root)
        top.title(title)
        top.geometry("350x200")  # Size for clear text display
        top.configure(bg="#34495e")
        
        # Label to display the message with word wrapping
        msg_label = Label(top, text=message, bg="#34495e", fg="#ecf0f1", font=("Helvetica", 12), wraplength=300)
        msg_label.pack(pady=20)
        
        def on_ok():
            # Close the message box and call the callback if provided
            top.destroy()
            if callback:
                callback()
        
        # OK button to dismiss the message box
        ok_button = Button(top, text="OK", command=on_ok, bg="#2ecc71", fg="white",
                           font=("Helvetica", 12, "bold"), relief=FLAT, bd=5, padx=15, pady=8)
        ok_button.pack(pady=10)

if __name__ == "__main__":
    root = Tk()
    app = FaultyCashbackSystem(root)
    root.mainloop()