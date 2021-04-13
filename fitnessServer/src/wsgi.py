# Copyright 2019 National Technology & Engineering Solutions of Sandia, LLC (NTESS). 
# Under the terms of Contract DE-NA0003525 with NTESS, the U.S. Government retains 
# certain rights in this software.
"""Run the Flask application"""
from app.app import create_app
app = create_app()


if __name__ == '__main__':
    app.run()

