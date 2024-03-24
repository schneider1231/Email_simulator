### --- OOP Email Simulator --- ###

# --- Lists --- #

inbox = []

# --- Functions --- #

class Email():
    # Class Variables
    has_been_read = False 

    def __init__(self, address, subject, content,):
        self.address = address
        self.subject = subject
        self.content = content
        
    def mark_as_read(self):
        self.has_been_read = True

def populate_inbox():
    # Create 3 sample emails and add it to the Inbox list. 
    email_1 = Email("John@example.com", "Heya", "Hi hope all is well.")
    email_2 = Email("Steevo@example.com", "Meeting", "Please find attached the meeting.")
    email_3 = Email("Hackerman123@example.com", "Job rejection", "Thanks for your time...")
    inbox.extend([email_1, email_2, email_3])


def list_emails():
    # Create a function which prints the email’s subject_line, along with a corresponding number.
    print("\nEmails:")
    for i, email in enumerate(inbox):
        print(f"{i + 1}. {email.subject}")


def read_email(index):
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    if 1 <= index <= len(inbox):
        email = inbox[index] 
        print("\nFrom:", email.address)
        print("Subject:", email.subject)
        print("Content:", email.content)
        email.mark_as_read()
    else:
        print("Invalid email Number.")

# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.
populate_inbox()

menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        # Logic to read an email
        list_emails()  # Display all emails
        email_index = int(input("Enter the index of the email you want to read: "))
        read_email(email_index - 1)  # Adjust index to match list indexing (starting from 0)
        
    elif user_choice == 2:
        # Logic to view unread emails
        print("Unread Emails:")
        unread_count = 0
        for email in inbox:
            if not email.has_been_read:
                print(f"From: {email.address} - Subject: {email.subject}")
                unread_count += 1
        if unread_count == 0:
            print("You have no unread emails.")
            
    elif user_choice == 3:
        #  Quit application
        print("Exiting application.")
        break

    else:
        print("Oops - incorrect input.")