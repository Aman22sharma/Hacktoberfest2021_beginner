from fastapi import FastAPI

app = FastAPI()

item_list = {
	1: {
		"name": "Snacks",
		"price": 12.34,
		"amount": 2
	},
	2: {
		"name": "Ice Cream",
		"price": 34.56,
		"amount": 1
	}
}

@app.get('/get_item/{item_id}')
def get_item(item_id: int):
	return item_list[item_id]