# Installation instructions
These instructions are meant for Windows.
## Installing Anaconda

- Go to [the downloads page of Anaconda](https://www.anaconda.com/download/success). 
- Download the Windows installer.
- Run the installer and complete the installation process. Do not change any of the preset settings unless you know what you are doing (you are reading this &#8594; you do not know &#8594; don't).
- Wait until the installation process is finalized.


## Installing VSCode

- Go to the [downloads page of VSCode](https://code.visualstudio.com/download).
- Download the Windows installer.
- Run the installer and complete the installation process. Do not change any of the preset settings unless you know what you are doing (you are reading this &#8594; you do not know &#8594; don't).
- Wait until the installation process is finalized.

## Installing Git
To download and keep track of the repository that contains all the exercises and theory, we will use `Git` in the console.
- Go to the [Git for Windows downloads page](https://git-scm.com/download/win).
- Download the installer (at the top of the page).
- Run the installer and complete the installation process. Do not change any settings.
- Once installed, go to your terminal or powershell of choice (`Anaconda prompt` included) and execute the following command:
```
git --version
```
- If the previous command worked, it means it is properly installed. 

## Setting up

- Run VSCode. A window should appear.
- Go to `Extensions` (looks like 4 squares).
- Search and install the `Python` extension.
- Search and install the `Jupyter` extension.
- Now your VSCode should be able to recognize all your anaconda python environments and use them to run any jupyter notebook. Test it and ask for help if this is not the case.

### Setting up the repository in your local machine

- First, choose the folder where you want the repo to be downloaded (the repo itself is a folder, so it is okay to have it somewhere like your Desktop folder).
- Now, within your terminal of choice, go to that folder (you can either go with the file explorer and right-click  and choose `Open in terminal` or use the commands `cd folder` and `cd ..` to navigate your file tree to get to your folder).
- Now you can download the repository for the course. To do so with `Git` you will generally use the command `git clone https://github.com/repository`. In this case, you have to run the following command:
```
git clone https://github.com/verzep/python_for_neuroscience
```
- Now you can just open the folder with VSCode (using the file explorer or the File option of the IDE) and start the good work!

-**Important**: If there need to be any corrections on the code from our end, run the command `git pull`. Try not to edit the errors yourself unless this does not work.

## Optional things
- (Optional) Launch `Anaconda Prompt` from the search bar. If you installed Anaconda for all users, you will need to run as an administrator. Run the command `conda update --all`. This will update all the installed packages (including defaults) to the latest version.