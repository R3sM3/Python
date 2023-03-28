Set up a development environment

1.- Install Visual Studio Code (if not already installed)
2.- Install Python (if not already installed)
3.- Create a directory for your code

        # Windows
        md contoso
        cd contoso

        ## macOS or Linux
        mkdir contoso
        cd contoso

4.- Create a virtual environment

        # Windows
        # Create the environment
        python -m venv venv
        # Activate the environment
        .\venv\scripts\activate

        # macOS or Linux
        # Create the environment
        python -m venv venv
        # Activate the environment
        source ./venv/bin/activate

5.- Install Flask and other libraries

        Name the file requirements.txt, and add the following text:

        flask
        python-dotenv
        requests

6.- Execute

        pip install -r requirements.txt