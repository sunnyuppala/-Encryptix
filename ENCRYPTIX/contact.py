import tkinter as tk
from tkinter import messagebox

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.contacts = {}

        # Create UI components
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.phone_label = tk.Label(root, text="Phone Number:")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(root)
        self.phone_entry.pack()

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(root)
        self.email_entry.pack()

        self.address_label = tk.Label(root, text="Address:")
        self.address_label.pack()
        self.address_entry = tk.Text(root, height=5, width=30)
        self.address_entry.pack()

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.pack()

        self.view_button = tk.Button(root, text="View Contact List", command=self.view_contacts)
        self.view_button.pack()

        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.search_button.pack()

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.pack()

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get("1.0", "end")

        if name and phone:
            self.contacts[name] = {"phone": phone, "email": email, "address": address}
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.address_entry.delete("1.0", tk.END)
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def view_contacts(self):
        contact_list = "\n".join([f"{name}: {phone}" for name, contact in self.contacts.items() for phone in [contact["phone"]]])
        messagebox.showinfo("Contact List", contact_list)

    def search_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()

        if name:
            if name in self.contacts:
                contact = self.contacts[name]
                messagebox.showinfo("Contact Found", f"Name: {name}\nPhone Number: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}")
            else:
                messagebox.showerror("Error", "Contact not found.")
        elif phone:
            for name, contact in self.contacts.items():
                if contact["phone"] == phone:
                    messagebox.showinfo("Contact Found", f"Name: {name}\nPhone Number: {phone}\nEmail: {contact['email']}\nAddress: {contact['address']}")
                    return
            messagebox.showerror("Error", "Contact not found.")
        else:
            messagebox.showerror("Error", "Please fill in a search field.")

    def update_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            self.contacts[name]["phone"] = self.phone_entry.get()
            self.contacts[name]["email"] = self.email_entry.get()
            self.contacts[name]["address"] = self.address_entry.get("1.0", "end")
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.address_entry.delete("1.0", tk.END)
            messagebox.showinfo("Success", "Contact updated successfully!")
        else:
            messagebox.showerror("Error", "Contact not found.")

    def delete_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            del self.contacts[name]
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.address_entry.delete("1.0", tk.END)
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showerror("Error", "Contact not found.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Contact Manager")
    contact_manager = ContactManager(root)
    root.mainloop()