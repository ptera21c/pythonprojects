import requests 


API_key = "<apikey>"
base_rul = "https://api.openweathermap.org/data/2.5/weather"


city = input("Enter a city: ")

request_url = f"{base_rul}?q={city}&appid={API_key}&units=metric"
response = requests.get(request_url)



if response.status_code == 200:
    data = response.json()
   
    main = data['weather'][0]['main']
    #print(main)
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    temp_min = data['main']['temp_min']
    temp_max = data['main']['temp_max']
    print(f"temperature: {temp}'c")
    print(f"minimum Temperature: {temp_min}'c")
    print(f"maximum Temperature: {temp_max}'c")
    print(f"it will feel like {feels_like}'c")
    
else:
    print("error occured")