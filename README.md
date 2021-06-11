# Playing card recognition 
This repository has the implementation of a playing card recognition tool, using open CV and python.

The interaction with the tool is done through the REST API interface, which has 2 interfaces so far.

1. To check a card.
	Accepts an image of **one** playing card.
	Returns the image of the corner of the card, and a guess of which one it is or an error.

2. To add a corner to the database
	Accept a card object:
		```
		{
			"number": str,
			"symbol": str,
			"image": bytes
		}
		```
	Returns status OK or error.

Other endpoints could be made for debugging in the beginning.

+ List all cards in the database
+ List all images in the database

## How to test

```sh
python -m unittest tests.test_core
```
