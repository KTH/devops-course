# COVID-19

## Students
Mindaugas Varkalys varkalys@kth.se @MindaugasVarkalys  
Justas Dautaras dautaras@kth.se @sonderangebot10

## Topic
Visualizing the places visited by infected people in Lithuania and matching them with Google Location history

## About the project
Last month we participated in [HackTheCrisis](https://hackthecrisis.lt/) hackathon in Lithuania and together with other team members built a project to visualize previously visited places by the infected people.
This data is provided by the Lithuanian government, but in very inconvenient format, so we visualized it on the map. 
We also created a feature to upload your Google Location history and see which infected places you visited. 
Apart from that, we worked with some epidemiologists and built a model, which calculates the likelihood of being infected depending on distance and time passed between your and the infected person's visits.
Based on the location data, we also calculate the amount of time spent outside, that way encouraging the people to better follow the quarantine.
We won the hackathon and afterwards we were contacted by [Eurovaistinė](https://www.eurovaistine.lt/) - the biggest pharmacy chain in Lithuania. We are now planning to work with them to display in our website the availability of masks in their pharmacies.
The project is hosted using [Netlify](https://www.netlify.com/) at [sekvirusa.lt](https://sekvirusa.lt).
The website is completely in Lithuanian language, but I think you should understand the main idea. It uses Continuous Deployment using Netlify.

## Repository of the project
https://github.com/arnas/tracking-virus-not-people

## Hosted project
https://sekvirusa.lt

## Mindaugas' contribution to the project

### Data extraction from Google Location history
The project has a feature to upload Google Location history to check if the user visited the infected locations.
There is no way to access Google Location history through Google API, so the only way for users to share their location history with our project is by using [Google Takeout](https://takeout.google.com/)
It allows to export and download various data collected by Google.
In our case, the user has to download the location history data and upload it to our website.
This process is quite complicated, so I created and added a short GIF image to the website, which shows how to do it.
When the exported data is uploaded, it has to be parsed and converted into the convenient format for further processing.
We decided to not send any data to the server side and do all the calculations on the client side to increase the trust of our product and ensure that the location data is not leaked, so all the code was written in JavaScript.
I analyzed the structure of the data file and wrote the algorithm, which parses the data into JavaScript array. The algorithm is implemented [here](https://github.com/arnas/tracking-virus-not-people/blob/master/app/src/features/uploadData/dataProcessing/parse.js)
The data file is in ZIP format which has a folder structure. One of the folders contains JSON files with the user location history. Each JSON file corresponds to a month.
However, it turned out that the folder names are dependant on the user's Google language settings, so their names cannot be hardcoded in my parsing algorithm. Thus, I decided to check each folder of the ZIP file for relevant file names.
Luckily, that was already implemented by the library, which I used for ZIP file reading, so it just returned all the available files in the ZIP file independently of the folder structure.
Function `chooseFiles` searches for 2 most recent JSON files in 2020 and returns their objects. 2 files are taken instead of 1 to avoid the case when the user uploads the data in the beginning of the month and the last file has less than 2 weeks of location history, which is needed in further processing.
The chosen files are parsed into JavaScript arrays and merged. The JSON files have 2 types of location data: visits and traveling. Function `processFilesData` filters the data leaving only visits having high or medium confidence.
The confidence is provided in the data and it allows to know the likeliness that the user actually visited that place. The function also converts the data into more convenient format to process and converts milliseconds into seconds.    

### Calculating the probability of being infected
Our website matches user's location history with the infected places and calculates the probability of being infected. The idea of the calculation algorithm was created by other team members, however its implementation in JavaScript was completely done by me.
The algorithm is implemented [here](https://github.com/arnas/tracking-virus-not-people/blob/master/app/src/features/uploadData/dataProcessing/process.js) and it works as follows:
- User's visited locations in the last 2 weeks are taken and the home/work visits are dropped. Home/work locations are found based on the amount of time spent there. If the user spent more than 10% of the time in that place and at least a single visit took more than 4 hours, it is treated as home or work place and it's not taken for further calculations.
- Each user's place visit is matched with infected places. If the visit took less than 3 minutes or there is no infected places in the radius of 50 meters or the place was visited before the infected person, the visit is treated as safe. Otherwise, the probability of infection is calculated using logistic regression depending on the time spent in the infected place.
Original implementation didn't have 3 minutes limit, however I added it later, because some users mentioned that the stops for the traffic lights in the infected area are treated as infected places' visits.
- All probabilities are combined and the final result of being infected is calculated. All the user's visits are ordered depending on the infection probability and shown to the user.   

### Calculating the time spent in public places
The website has a feature to show how much time the user spent at home and how many public places he/she visited. The result can be shared on the social media, so it should encourage others to better follow the quarantine.
The algorithm is implemented [here](https://github.com/arnas/tracking-virus-not-people/blob/master/app/src/features/uploadData/dataProcessing/futureRisk.js). It works as follows:
- To find public places I analyzed Google Location history data and found that the public places always have different name than the address.
For example, supermarkets, museums, parks, etc. always have meaningful names, however, private places like living houses always have the same name as the address.
I didn't want to include private places visits for this calculation, because visiting a private place is not that dangerous compared to public place. So depending on whether the name matches the address I filtered the public places.
- I grouped all the visits of the same place and calculated the total time spent at that public place.
- I found the home address by using the algorithm described earlier and calculated time spent at home.
- I calculated the percentage of time spent at home out of 12 hours a day. I took 12 hours instead of 24, because most people usually spend at least 12 hours a day at home while sleeping or preparing to sleep.
So the maximum amount of time the person can spend in public places is around 12 hours.
- All the calculated information is shown to the user: percentage of time spent at home, visited public places and the number of hours spent in public places.
   
