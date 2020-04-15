# Shopping Cart Project
## Installation
Fork this repository, clone it (choose a familiar download location such as Desktop). Then, navigate to your repository from command line:
```sh
cd ~/'download location'/shopping-cart
```
## Setup
Consider creating a virtual environment called something like shopping-env:
```sh
conda create -n shopping-env python=3.7 # (first time only)
```
Then, activate your virtual environment:
```sh
conda activate shopping-env
```
However, the code should work in your base environment
## Usage
To run the script, type the following in the command line
```sh
python shopping_cart.py
```

No you should be able to enter the ids of the selected products.
Once you are done, type "Done"
The script will return the receipt including all the selected items

## Testing

Install the pytest package with a virtual environment:
```sh
pip install pytest
```
Run tests:
```sh
pytest
```

if you have any questions regarding the application, please contact me at grocery@piedpiper.edu

