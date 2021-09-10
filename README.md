# DataZCW-Final-Project
capstone project for ZCW Data's course.

Dog Days of the Year


Problem:

-	Once a sports season is over (especially the dog days of the summer) people struggle to find content on their favorite sport
-	This will give people a way to check on diffrenet sports and their upcoming schedule.  it will allow them to search for sporting events while out of town and a chance to check in on a new sport.


Methods/Collect:


-	Scrape sports api sites for season schedules and fan friendly events
  - Api used https://sportradar.us/ - (Sportradar)
  -Scraped MLB,NHL,NFL,NBA
- Postman

Clean:

-	Creat a dataframe to clean api's and insert into a Dag for Airflow 
-	Create a Database using Python and SQL to show cleaned up data using columns and rows for an applicaion 

Data Pipeline:

-	Scrape viewing platforms for all sports 
-	Collect schedules for all major sports
-	Filter out all irrelevant information
-	Store it into a dataframe
-	Get engine working to filter out data producing any changes in schedules and why 

Create visualization:
- Pie Chart of each sport showing how many months its regular season lasts and at what percentage
- Line Chart comparing sports peak months against each other


 
Recommendation Engine:
- Get engine working to filter out data producing recommendations based off sports preferences along with location, and possibly favorite team
