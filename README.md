# What is this project ?

This project is a new version of the snake game popularized by Nokia in the 90s. This version is coded in Python. As for the graphical interface, the game uses the [turtle package](https://docs.python.org/fr/3/library/turtle.html).

# Requirement

Before launching the game, you need to make sure one last thing: check that python is installed on your computer. Type in a terminal:

```sh
python --version
```

If you see a message like:

```
Python 3.8.10
```

Python is installed. But if an error message appears, go to the [official website](https://www.python.org/) of python, go to the [download page](https://www.python.org/downloads/) and follow the instructions for your operating system.

# Run the game

To play the game, there are several steps to follow:

* You must first download the source code. To do this, go to the project [home page](https://github.com/Debboss/Snake-Game), press the green "<> Code" button, go to the "Local" tab and select "Download ZIP".
* Now unzip the ZIP file that appeared in your downloads.
* When done, open a terminal and go to the unzipped folder with the cd command. For example:

    ```sh
    cd Downloads/Snake-Game-main/src/
    ```

* Now type:

    ```sh
    python main_snake.py
    ```

    And enjoy the game!

# You want to contribute ?

If you want to contribute to this project you are welcome! For this, there are a few steps:

1. Create a project fork in your github account.
2. Clone this fork on your machine with:

    ```sh
    # make sure that git is installed before doing this
    git clone https://github.com/your-username/Snake-Game
    ```

3. Create a new branch that describes what you want to do by entering:

    ```sh
    git checkout -b my-branch
    ```

4. Make your changes.

5. Add the files you have modified:

    ```sh
    git add .
    ```

6. Make a commit where you say everything you’ve done:

    ```sh
    git commit -m "I changed... and I added..."
    ```

7. Push your changes to github:

    ```sh
    git push origin my-branch
    ```

8. Make a pull request by going to the project fork page and clicking on "Contribute > Open pull request". A window will open and you will be able to explain in more detail all the changes you have made.

9. Validate and then wait... :-)
