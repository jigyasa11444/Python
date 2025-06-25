import requests
import csv
import os


def get_movies_titles():
    """Takes inputs from the user """
    print("Enter the Title and Year")
    title = input("Title: ")
    return title
     
   

def fetch_movie_data(title):
   base_url = "http://www.omdbapi.com/"
   params = {
       "t" : title,
       "apikey" : "af60a0ec"
   }

   response = requests.get(url=base_url, params = params )

   if response.status_code == 200:
       data = response.json()
       if data.get("Response") == "True":
           return {
               "Title": data.get("Title"),
               "Year": data.get("Year"),
               "Genre": data.get("Genre"),
               
           }
       else: 
           print("Movie not fount: ", data.get("Error"))
           return None

   else:
       print("Failed to fetch data. status code: ", response.status_code)  
       return None 
       

def save_to_csv(movieData, filename="resource.csv"):
    fieldnames = ["Title", "Year", "Genre", "IMDB Rating"]
    fileExist = os.path.isfile(filename)
    

    try:
        with open(filename , mode= "a", newline="", encoding="utf-8" ) as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames )

            if not fileExist or os.stat(filename).st_size == 0:
               writer.writeheader()

            writer.writerow(movieData)
            print(f"Movie '{movieData['Title']}' saved to {filename}.")   


    except Exception as e:
        print("Error writing to CSV:", e)


   
def main ():
   Title =  get_movies_titles()
   movieData = fetch_movie_data(Title)

   if movieData :
    save_to_csv(movieData, filename="resource.csv")
   else:
      print("No data to save") 

if __name__ == "__main__":

 main()