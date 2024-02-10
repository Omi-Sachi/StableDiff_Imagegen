import tkinter as tk
import customtkinter as ctk 
from customtkinter import CTk, CTkEntry, CTkButton

from PIL import ImageTk
from authtoken import auth_token

import torch
from torch import autocast
from diffusers import StableDiffusionPipeline 

# Create the app
app = tk.Tk()
app.geometry("532x632")
app.title("Let's get Creative") 
ctk.set_appearance_mode("dark") 

prompt = ctk.CTkEntry(master=app,
                               width=450,
                               height=40,
                               corner_radius=10, fg_color='#98FB98', text_color="white", placeholder_text='What will you create!:', font=('Chiller',20))

prompt.place(x=10, y=450)
img_frame = ctk.CTkLabel(master=app, height=400, width=510 )
img_frame.place(x=10, y=10)

#Model
#modelid = "CompVis/stable-diffusion-v1-4"
#device = "cuba"
#pipe = StableDiffusionPipeline.from_pretrained(modelid, revision="fp16", torch_dtype=torch.float16, use_auth_token=auth_token) 
#pipe.to(device) 
#Where our image will generate
#def generating():
 #    with autocast(device): 
  #      image = pipe(prompt.get(), guidance_scale=8.5)["sample"][0]
    
   #  image.save('generatedimage.png')
    ## img = ImageTk.PhotoImage(image)
     #img_frame.configure(image=img) 

generate = ctk.CTkButton(master=app, width=50, height=40, fg_color='#ADD8E6',hover_color='grey', text_color='black', text='Send', hover=True) #command=generating)
generate.place(x=470, y=450)

app.mainloop()