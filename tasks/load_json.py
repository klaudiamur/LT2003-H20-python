import json
import pandas as pd

def load_json():
	with open('json_data.json','r') as f:
		#load json_data.json file
		data = json.load(f)
		#extract the sentences from json_data
		rows = []
		for x in data:
			x_row = x['words']
			y = x['id']
			
			for row in x_row:
				row['id'] = y
				rows.append(row)
		df = pd.DataFrame(rows)
		df_s = df.set_index('id')
		df.columns = ['|word_id |','word |','|sentence_id|']
		print(df_s)
		
 
if __name__ == '__main__':
	load_json()
	
	
	
	
