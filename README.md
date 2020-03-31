# HU-grade-crawler
Crawls grades from student records of the Humboldt-University and sends SMS with new grades

The tool uses MechicalSoup to access the student records of the Humboldt-University Berlin, log-in, navigate to the module
results and crawl the data. Using a cron job the script can be run every ten minutes during working hours to crawl the grades.
After the initial crawl it will compare the newly crawled data. If the script detects a new grade, it will send a SMS containing
the new grade to a predefined number.

**Be a good internet citizen and crawl kindly! NEVER run several concurrent instances of this script (one says the HU's servers are not too stable), don't shorten the waiting times in the script and don't crawl to often.**

### Prerequisites

You need to install Python and the package manager PIP. When you install Python <= 3.4 from the [official website](https://www.python.org/downloads/), PIP is already installed.

```
# Install virtual enviroment
pip install virtualenv
```

### Installation

First set-up and start the virtual environment.

```
# Create virtualenv
virtualenv -p python3 huc

# Start environment
source huc/bin/activate

```

Now clone the repo to the "src"-folder or download the [repo](https://github.com/fbennets/HU-grade-crawler) as zip, unpack the folder, move it into the folder of your environment and rename it to "src".

```
# Clone repository to current directory
cd huc
git clone https://github.com/fbennets/HU-grade-crawler.git src

```
Next install the requirements.

```
# Install dependencies
cd src
pip install -r requirements.txt
```

### Set-up

Now, go to [Twilio](https://www.twilio.com), create an Account, obtain a mobile number and get your credentials. Search online for Twilio Quest if you fancy some free credits. 

Open the creds.py file and insert your student records credentials, your Twilio credentials and you own mobile number (not the Twilio one). 

Run 
```
python mech.py 
```
in the project root to create the initial dataset. Afterwards push everything to a cheap server like [Uberspace](https://uberspace.de/en/) and set up a cron-job to run the script e.g. every ten minute during working hours.
