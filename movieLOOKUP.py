import http.client

conn = http.client.HTTPSConnection("utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "SIGN-UP-FOR-KEY",
    'X-RapidAPI-Host': "utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com"
}

conn.request("GET", "/lookup?term=bojack&country=uk", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))