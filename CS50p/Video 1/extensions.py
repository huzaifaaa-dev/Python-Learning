# Check the name of a file provided by the user and match it to file types.
filename = input("File Name: ")
if filename.endswith(".gif"):
    print("image/gif")
elif filename.endswith(".jpg") or filename.endswith(".jpeg"):
    print("image/jpeg")
elif filename.endswith(".png"):
    print("image/png")
elif filename.endswith(".pdf"):
    print("application/pdf")
elif filename.endswith(".txt"):
    print("text/plain")
elif filename.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")

# The following code will NOT work.
# Explained in my Experiments repository, File: Experiment-1.md .
match filename:
    case filename.endswith(".gif"):
        print("image/gif")
    case filename.endswith(".jpg") | filename.endswith("jpeg"):
        print("image/jpeg")
    case filename.endswith(".png"):
        print("image/png")
    case filename.endswith("pdf"):
        print("application/pdf")
    case filename.endswith("txt"):
        print("text/plain")
    case filename.endswith("zip"):
        print("application/zip")
    case _:
        print("application/octet-stream")
