
import sys
import clipboard
import json


def save_items(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)
        
def load_items(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

def delete_items(filepath,key):
    with open(filepath, "r") as f:
        data=json.load(f)
        del data[key]
    with open(filepath, "w") as f:
        json.dump(data, f)


SAVED_DATA = "clipboard.json"

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_items(SAVED_DATA)
    
    if command == "save":
        key = input("Enter a key: ")
        data[key]= clipboard.paste()
        save_items(SAVED_DATA, data)
        print("saved to clipboard!")
    
        
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("copied to your clipboard")
        else:
            print("the key does not exist!")
    
            
    elif command == "list":
            print(data)
    
    elif command =="delete":
        key = input("Enter a key you want to delete: ")
        if key in data:
            delete_items(SAVED_DATA,key)
            print("{} has been deleted from clipboard".format(key))
        else:
            print("the key does not exist")
    else:
        print("unknown command")
    
else:
    print(" you need to put one argument")