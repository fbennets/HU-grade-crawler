# HU-grade-crawler
Crawls grades from student records of the Humboldt-University and sends SMS with new grades

The tool uses MechicalSoup to access the student records of the Humboldt-University Berlin, log-in, navigate to the module
results and crawl the data. Using a cron job the script can be run every ten minutes during working hours to crawl the grades.
After the initial crawl it will compare the newly crawled data. If the script detects a new grade, it will send a SMS containing
the new grade to a predefined number.
