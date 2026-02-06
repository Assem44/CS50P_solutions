file_name = input("File name: ").lower().strip()
extension = ""
if ("." in file_name):
    index_of_last_dot = file_name[::-1].index('.') # for file name like that : filename.me.pdf
    extension = file_name[-index_of_last_dot:]
match extension :
    case "png" | "jpg" | "jpeg" | "gif":
        print(f"image/{"jpeg" if extension == "jpg" else extension}")
    case "pdf" | "zip":
        print(f"application/{extension}")
    case "txt":
        print(f"text/plain")
    case _:
        print("application/octet-stream")
