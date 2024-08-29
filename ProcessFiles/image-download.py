image_data = client.files.content("file-x6YV6lMHUF44eC03mKiVVR56")
image_data_bytes = image_data.read()

with open("./my-image.png", "wb") as file:
    file.write(image_data_bytes)s