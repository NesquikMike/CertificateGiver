# Certificate Giver
This markdown file is an instructional guide on how to use the Certificate Giver.

## Set Up

  I have already installed the Certificate Giver on your computer and the accompanying packages that you will need 
  for it like Pandas. So all you have to do now is go into the right folder and do a Git Pull to get the latest 
  version.  
  
  1. First step then is to open your Terminal.
  
  2. Now let's check that we are in the right place. Let's recap you should remember some of this from the Report 
  Writer. Although don't worry if you don't since it has been a while since you last used that! Into your terminal 
  let's type in `pwd` (which stands for "present working directory") after the dollar sign and 
  press Enter. You should get something that looks like this:

        ```bash
        Honigs-MacBook-Air:~ honigschnitzel$ pwd
        /Users/honigschnitzel
        ```
     For future reference from here on in I will write all of the code that you should enter into the terminal after a 
     dollar sign and the expected result on the line below, if the line below starts with a `$` then that is a new 
     instruction for the computer once you have entered the previous line, it also implies that there will probably be 
     no output. Thus, the previous instruction and result would appear like this:
     
        ```bash
        $ pwd
        /Users/honigschnitzel
        ```
      But there is no need to type the dollar sign, it merely signifies code to type in.
    
  3. Now before we move to the folder we need to go to, let's check that the folders are structured as expected. Do `$ ls` (Remember there is no need to type the dollar sign, it should already be on the last line of 
  your terminal!) such that you can get a list of files and 
  folders in your home directory, like so:
        ```bash
        $ ls
        Applications		Public			projects
        Desktop			i<3HonigSchnitzel.docx  server.R
        Documents		bash_profile		testGame1.R
        Downloads		go			testGame2.R
        IdeaProjects		hello.py		ui.R
        Library			mpsGame1.R		venv
        Movies			my_oauth		xkcd.ttf
        Music			placeNamesFilter.csv
        Pictures		probRetention.R
        ```
        
     No doubt your list of folders and files will look different to this but it should look similar. Now we should be 
     ready to move to where we need to be. Move into documents by doing `$ cd Documents` you should have no output 
     such that the computer is now ready to accept a new instruction:
     
        ```bash
        Honigs-MacBook-Air:~ honigschnitzel$ cd Documents
        Honigs-MacBook-Air:Documents honigschnitzel$
        ```
      Notice that the `~` has been replaced by `Documents`. This is because you are no longer in your Home directory 
      (a directory is a folder), but you are now in Documents. Whatever follows the colon is always the name of 
      your current folder in the Terminal.

  4. We're over half way through the set-up process, so nearly there! Let's move into the `CertificateGiver` folder and 
  then do a `$ git pull` to get the latest update:
  
        ```bash
        $ cd CertficateGiver
        $ git pull
        remote: Counting objects: 3, done.
        remote: Compressing objects: 100% (3/3), done.
        remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0
        Unpacking objects: 100% (3/3), done.
        From https://github.com/NesquikMike/CertificateGiver
           18c38b4..a763eb3  master     -> origin/master
        Updating 18c38b4..a763eb3
        Fast-forward
         README.md | 44 +++++++++++++++++++++++++++++++++++++++++++-
         1 file changed, 43 insertions(+), 1 deletion(-)
        ```
        
  5. We're now ready to make a spreadsheet suitable for all the kids in your class. This bit is really easy and you 
  hopefully won't have to do it again this academic year. You will have to answer the following where `[Class Size]` is 
  a number equal to the number of children in your class. 
  
        ```bash
        $ python3 dummyExcelMaker.py [Class Size]
        ``` 
        
     To give an example if you had a class of 25 children you would enter:
     
        ```bash
        $ python3 dummyExcelMaker.py 25
                             Names
        0          Guadalupe Siers
        1              Tyree Truan
        2   Marcelino Hollingworth
        3             Gaston Smith
        4             Honey Flaggs
        5              Gaston Beer
        6        Herminia Guzewicz
        7              Isela Stieb
        8            Maurice Hyten
        9           Federico Steeb
        10             Vito Daking
        11          Cecile Thramer
        12       Benita Muhlenkamp
        13         Winfred Demmert
        14           Aaron Shaheen
        ``` 
        
  6. Last step we need to do manually, unfortunately, is open up the CSV we have just made in the last step in 
  Microsoft Excel and replace the fake names with the real names of the kids in your class. We can do this in the 
  normal way without the terminal by going into Finder and going into your Documents folder and then into your 
  CertificateGiver folder and then opening the classSpreadsheet.csv from there. But, let's be fancy and take a shortcut 
  using the terminal, enter the following into the terminal (Don't forget to save you typing out big file or directory 
  names, once you have typed in the first few letters of the file or directory you can usually press the Tab button 
  for the Terminal to finish what you have written for you!): 
  
        ```bash
        open classSpreadsheet.csv
        ```
        
     This should open the CSV for you in Microsoft Excel. You're all set to change the names now, just make sure when you 
     save your changes you don't change the name of the CSV, or the Certificate Giver will not work. When you have 
     finished close your terminal. 
  
We've finished setup and now we are ready to use the Certificate Giver! Good work, You're becoming a real Pro with 
the terminal!
  
## Using the Certificate Writer

  1. Open your Terminal and move into your Documents folder by doing (don't forget you can use Tab to predict 
  directory and file names once you have typed a few letters with the Tab button):
        
        ```bash
        $ cd Documents
        ```
        
      If you need to, you can check that the CertificateGiver folder is in here by doing `$ ls`, which will list all 
      the files and folders in your Documents folder. `CertificateGiver` should be listed among them.
  
  2. Move into the CertificateGiver folder by doing:
        
        ```bash
        $ cd CertificateGiver
        ```
  
  3. We're ready to start giving some certificates! To give out certificates we should type the following, where 
  `[Certificates to Give]` and `[Weeks to Ignore]` are optional and have default values of 2 and 3 respectively:
  
        ```bash
        $ python3 certificateGiver.py [Certificates to Give] [Weeks to Ignore]
        ```
  
      Since the default values for `[Certificates to Give]` and `[Weeks to Ignore]` are 2 & 3 respectively entering the 
      the command below into the Terminal will give 2 certificates and will ensure that any child that has received a 
      certificate in the last 3 occasions that you have given a certificate will not get a certificate:
      
        ```bash
        $ python3 certificateGiver.py 
        CERTIFICATES FOR: 
        Fritz Durnin
        Gaston Illich
        SPREADSHEET HAS BEEN UPDATED
        ```
            
      After running this the CSV will now also be updated so you can consult this at a later date. If instead you wanted to 
      change the number of certificates to give this week or to change the number of certificate giving weeks to ignore 
      when deciding to give certificates, you will need to those optional parameters like so:
      
        ```bash
        $ python3 certificateGiver.py 5 5
        python3 certificateGiver.py 5 5
        CERTIFICATES FOR: 
        Nada Kinkelaar
        Theron Bramlett
        Emmitt Demmert
        Kaylene Osterholt
        Thomas Whyne
        SPREADSHEET HAS BEEN UPDATED
        ```
            
      This has given 5 certificates to the 5 children and ensured that anyone who has gotten a certificate in the last 
      5 occasions that certificates were given has not gotten another certificate. 
      
      Now that the certificates have been given you can just make a note of the names that appear on the Terminal as 
      they have been recorded in the spreadsheet; you don't need to do anything to the CSV for the changes to be 
      recorded. You can check them in the CSV to if you prefer or if you want to see who got certificates in previous 
      weeks. Remember you can open the CSV from the terminal by using the command:
      
      ```bash
      $ open classSpreadsheet.csv
      ```
      
      A quick note, if you run the Certificate Giver more than once in the same day it will give you the option to 
      overwrite the previous certificates, or to maintain the certificates already given for the current day. This can 
      be useful if you don't agree with the children selected by the Certificate Giver and would prefer it to choose 
      different pupils. If you need to give more certificates than are currently given for today, it is better to run 
      it again choosing to give to a higher number of pupils and overwrite the current selection. You can choose to 
      overwrite or not by pressing either `y` (yes) or `n` (no) into the Terminal when given the choice to overwrite 
      or not. As always let me know if there are any issues! Happy Certificate Giving!