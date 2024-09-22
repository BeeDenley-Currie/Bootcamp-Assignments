# CFG-Assignments
## `Hello World`! Welcome to my readme! 👋

My name is Bee, and I'm on the *Data Science* pathway of the Autumn 2024 CFGdegree. I'm being sponsored by [DSTL](https://www.gov.uk/government/organisations/defence-science-and-technology-laboratory).

- I have previously completed a number of different CFG coding courses, as well as making the most of external learning opportunities
  
> [!NOTE]
> I have 2 cats (who are the best), they are <sup>Felix</sup> and <sub>Moose</sub> 🖤🤍🖤
>
> <img src="https://github.com/user-attachments/assets/b48ee013-c50a-4e4a-b357-22309eed45ce" width="200" /> <img src="https://github.com/user-attachments/assets/0f43f37b-9d3f-47dd-ac84-9bbf35a47edd" width="200" />

I am planning to use this repository to submit my various assignments, this profile as a whole may also be used as a resource for new information I learn along my coding journey. 
<details>
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

  I have created a database for for animal viruses, with core tables being virus information, species, tests offered, and sample types
There are then additional tables for susceptibility for animals, and acceptable tests for sample types.
Further, I have a customers table, and a combination of different information all comes together in the orders table.

Lines <b>1 - 230</b> of my code are creating the database and entering the values.

This is an EER of my relational database:
![EEV 220924](https://github.com/user-attachments/assets/3dbc1459-6b24-4b32-808c-43a79325a7aa)

### Creative Scenario
I'm imagining this database as useful within animal virology/laboratory testing fields, but the same concept can of course be applied to may different commercial science areas.
- [X]  As an example, this database is functional to ensure that a new order meets the testing/sampling requirements (i.e. have they sent the right sample type for the test they need?)
- [X]  It is also useful to be able to update the database as new sample types are approved for testing (like adding plasma as an acceptable sample type for ELISA testing)
- [X]  We can see what viruses are requested for testing the most, to give insights into what will need extra stocks bought vs a rarely ordered test.

</details>
