# value ko string se json mein convert karna aur json ko string mein convert karna 
import json 


def laod_data():
    try:
        with open('youtube.txt','r') as file:
            # yeh json mein convert kar dega. 
            return json.load(file)
    except FileNotFoundError:
        return []

# json.load = load matlab sara data load kar do 
# josn.dump = dump matlab sara data write kar do.

def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)
    

def list_all_videos(videos):
    # enumerate() yeh indexing karne ka kam karta h. 
    for index, video in enumerate(videos,start=1):
        print(f"{index}")

def Add_videos(videos):
    name = input("enter video name: ")
    time = input("enter video time: ")
    videos.append({'name':name, 'time':time})
    save_data_helper(videos)


def update_videos(videos):
    pass

def delete_videos(videos):
    pass

def main():
    videos = laod_data()

  


    while True:
        print("\n youtube manager | choose an option")
        print("1.List all youtube videos")
        print("2.Add youtube videos")
        print("3.update a youtube video details")
        print("4.delete a youtube video details")
        print("5.exit the app")
        choice =  input("Enter your choice")
        print(videos)
        

        match choice:
            case '1':
              list_all_videos(videos)
            case '2':
              Add_videos(videos)
            case '3':
              update_videos(videos)    
            case '4':
               delete_videos(videos)  
            case '5':
               break

            case _:
              print("invalid choice")

# agar function ka nam main hai toh kahin pe bhi is file ke andar toh main ko run kar do.
if __name__ == "__main__":
    main()