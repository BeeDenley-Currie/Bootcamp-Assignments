# Bootcamp-Assignments

My name is Bee, and I have recently completed the *Data Science* pathway of an intensive Bootcamp, sponsored by [DSTL](https://www.gov.uk/government/organisations/defence-science-and-technology-laboratory).

- I have previously completed a number of different CFG coding courses, as well as making the most of external learning opportunities
  
I have removed mentions of the bootcamp providers name. 
<details open>
  <summary>Assignment 1</summary>
<h3>Assignment 1</h3>

1. I created this repository on Github, and then cloned it to my local repository.  
2. With this, I have checked the status, and created the "new-branch" branch. This is where I added the empty requirements.txt file, and then committed this change while explaining the addition. Both branches were then pushed to the remote repository
<img src="https://github.com/user-attachments/assets/72537cbc-37b3-4dd9-a8d4-8b0d765ad359" alt="Git Code Examples" width="500"/>

3. On Github I created a pull request,
<img src="https://github.com/user-attachments/assets/361f63a2-e8e8-4aa0-ba88-1b051e2d4209" alt="Pull Request" width="500"/>

4. I then merged that pull request.
<img src="https://github.com/user-attachments/assets/96b3f6ca-4e30-4354-a963-c8cecc40b50f" alt="Merge and Deploy" width="500"/>

5. And finally I have used `git pull` to keep my local repository up to date.
<img src="https://github.com/user-attachments/assets/62219e55-5248-4e68-97f6-f076c72ab3ad" alt="Git pull from main to local" width="500"/>
</br>
</br>

> The [requirements.txt](/requirements.txt) file is a list of the necessary libraries/packages and their version numbers to be installed for the code in the repository to work. These are not included in the project folder itself, but instead the file is a list that can then be downloaded in your IDE, using a command like `pip install -r requirements.txt`. Requirements.txt makes it easy for others to use your project, as they can easily install required packages.
> The version numbers are important because some features may not be available in all versions of a package, which could cause your code not to work.

Within this repository I have also created a :
- [X] [.gitignore](/.gitignore) file
> .gitignore files are important because they hide certain files from `git status` and means that these files are not selected using commands like `git add`. Depending on what the repository is being used for, there may be a large amount of data and code for different libraries used in the files but which you wouldn't want to download each time, as it will bloat the downloads. It can be set to ignore personal information, for example if there's a file with login details.</br>
In this case I have chosen a standard .gitignore file for python, but the .gitignore file is not mandatory when creating a repo - just a good idea!
</details>

<details open>
<summary>Assignment 3</summary>
  <h3>Assignment 3</h3>

### Creative Scenario
I am creating a (fictional!) database to help my animal infectious disease laboratory (fictionally!) keep track of our testing needs, and our orders from customers.
I have created core tables: virus information, species, tests offered, and sample types. Much of my data is just for the back-end, but needs to be normalised into different tables so that we can make updates to naming without ruining the whole DB!
There are then additional tables for susceptibility for animals, and acceptable tests for sample types, which can be updated as a situation develops/more research is done.
Further, I have a customers table, and a combination of different information all comes together in the orders table.

- [X] I have inserted values, as well as written queries to alter/update portions of the original tables, using constraints such as NOT NULL and DEFAULT. Data types include DATE, ENUM, VARCHAR, and INT. Order ID is an AUTO INCREMENT value.
- [X] I have created views which join different tables, to make the information much more human-readable, using INNER JOIN
- [X] Using LEFT JOIN, I am able to discern if there are samples with no accepted tests
- [X] I wanted to be able to find where an order did/didn't meet test/sample requirements for the virus. I found a couple of different methods, first using a LEFT JOIN and a WHERE EXISTS subquery but-
- [X] I then created a Stored Function so that it will be more obvious which ones are possible/impossible to fulfill.  
- [X] I was able to fix spelling mistakes, and because of the normalisation this means changes can be made to the string without ruining other dependent tables.
- [X] I wanted to find a way to show the due date of an order, with 2 different interval periods depending on customer type. I did this using subqueries, CASE, DATE_ADD, and a hefty dose of trial and error!
- [X] I've used aggregate functions to provide information on how many species are susceptible for each virus (handy for deciding what research will have the most impact) using COUNT, and to find the oldest order for each customer in the UK using MIN. I found it difficult to give good examples because my database is so text heavy!
- [X]  It's important to be able to DELETE data from a table without it messing everything else up, so I demonstrated that I can remove from a table without issue

As far as future work:
- [ ]  We could see what viruses are requested for testing the most, to give insights into what stock levels we need for different assays

A Database like this is useful within animal virology/laboratory testing fields, but the same concept can of course be applied to may different commercial science areas.


- Lines <b>1 - 230</b> of my code are creating the database and entering the values
- Lines <b>231 - 278</b> demonstrate <u>joins</u>, by creating <u>views</u> and during select queries
- Lines <b>279 - 310</b> create and demo a <u>stored function</u> (proud of this bit!)
- Lines <b>311 - 357</b> show off a couple of additional <u>in-built functions</u>, and updating tables based on another table's values (also really proud of this bit!)
- Lines <b>358 - 372</b> are the <u>aggregate functions</u>. 
- Lines <b>373 - 378</b> are a <u>delete</u> query, and a further query to prove it worked

This is an EER of my relational database:
![EEV 220924](https://github.com/user-attachments/assets/3dbc1459-6b24-4b32-808c-43a79325a7aa)

</details>
