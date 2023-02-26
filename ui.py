"""User Interface module for Get ESET Product Code project"""

_VERSION = "0.1.0" # The program version that will be displayed on the UI

import customtkinter
import eset

class MainWindow(customtkinter.CTk):
    """Main GUI window"""

    titletext = "Get ESET Product Code"

    def __init__(self) -> None:
        super().__init__()
        # Window
        self.title(self.titletext)
        self.geometry("400x200")
        self.resizable(False,False)
        self.grid_rowconfigure(0, weight =1)
        self.grid_columnconfigure(0, weight =1)
        # Frame
        self.frame = customtkinter.CTkFrame(self)
        self.frame.configure(border_width=5)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.grid_rowconfigure(2, weight=1)
        # Title
        self.titlebanner = customtkinter.CTkLabel(self.frame)
        self.titlebanner.configure(text=self.titletext, font=("Arial", 20, "bold"), height=50)
        self.titlebanner.grid(row=0, column=0, columnspan=2, sticky="nwe", padx=5, pady=5)
        # Input
        self.inputuuid = customtkinter.CTkEntry(self.frame)
        self.inputuuid.configure(placeholder_text="Enter the UUID here...", justify="center", border_width=0, height=40)
        self.inputuuid.grid(row=1, column=0, columnspan=2, sticky="nwe", padx=15, pady=5)
        # Button
        self.submitbutton = customtkinter.CTkButton(self.frame)
        self.submitbutton.configure(text="Convert to Product Code", anchor="center", height=40, fg_color="Green", hover_color="DarkGreen", command=self.convert)
        self.submitbutton.grid(row=2, column=0, columnspan=2, sticky="nwe", padx=15, pady=15)
        # Footer
        self.footerbanner = customtkinter.CTkButton(self.frame)
        self.footerbanner.configure(text=f"Version {_VERSION}", font=("Arial",10), height=20, fg_color="transparent", hover=False, command=lambda: AboutWindow())
        self.footerbanner.grid(row=3, column=0, columnspan=2, sticky="s", padx=5, pady=5)

        self.mainloop()
    
    def convert(self) -> None:
        """Converts entered UUID to Product Code
        
        Gets UUID from entry box and passes to get_product_code.
        Displays the returned value in the entry box.
        """
        uuid = self.inputuuid.get()
        productcode = eset.get_product_code(uuid)
        self.inputuuid.delete(0,len(uuid))
        self.inputuuid.insert(0,productcode)

class AboutWindow(customtkinter.CTkToplevel):
    """About dialog window"""

    titletext = "Get ESET Product Code"

    def __init__(self) -> None:
        super().__init__()
        # Window
        self.title("About")
        self.geometry("400x200")
        self.resizable(False,False)
        self.grid_rowconfigure(0, weight =1)
        self.grid_columnconfigure(0, weight =1)
        self.grab_set()
        # Frame
        self.frame = customtkinter.CTkFrame(self)
        self.frame.configure(border_width=5)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(2, weight=3)
        # Title
        self.titlebanner = customtkinter.CTkLabel(self.frame)
        self.titlebanner.configure(text=self.titletext, font=("Arial", 20, "bold"))
        self.titlebanner.grid(row=0, column=0, columnspan=2, sticky="nwe", padx=5, pady=5)
        # Version
        self.versionbanner = customtkinter.CTkLabel(self.frame)
        self.versionbanner.configure(text=f"Version: {_VERSION}", font=("Arial", 13))
        self.versionbanner.grid(row=1, column=0, columnspan=2, sticky="nwe", padx=5, pady=0)
        # Detail Frame
        self.detailframe = customtkinter.CTkFrame(self.frame)
        self.detailframe.grid(row=2, column=0, columnspan=2, sticky="nwe", padx=5, pady=0)
        self.detailframe.grid_columnconfigure(0, weight=1)
        self.detailframe.grid_rowconfigure(1, weight=1)
        # Details
        self.detailline1 = customtkinter.CTkLabel(self.detailframe)
        self.detailline1.configure(font=("Arial", 11), justify="center", corner_radius=2,
                                   text=("\nPatrick Cage (patrick@patrickcage.com)\n"
                                         "\nPlease file bug reports at https://github.com/patrickcage/get-eset-product-code\n"
                                         "\nThis product is not supported, endorsed or otherwise linked to ESET."))
        self.detailline1.grid(row=0, column=0, columnspan=2, sticky="nwe")
        # Web URL
        self.weburl = customtkinter.CTkLabel(self.frame)
        self.weburl.configure(text="www.patrickcage.com", font=("Arial", 11))
        self.weburl.grid(row=3, column=0, columnspan=2, sticky="swe", padx=5)


if __name__ == "__main__":
    print(f"\nGet ESET Product Code (ui.py)")
    print("By Patrick Cage (patrick@patrickcage.com)")
    print("This module is intended to be imported by main.py\n")
