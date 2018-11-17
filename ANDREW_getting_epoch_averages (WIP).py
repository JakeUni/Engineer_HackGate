import requests
epoch_res = requests.get('http://egchallenge.tech/epoch').json()
current_epoch = epoch_res['current_epoch']
prediction_epoch = epoch_res['prediction_epoch']
timestamp = epoch_res['unix_timestamp']
print(f'current_epoch = {current_epoch}, prediction_epoch = {prediction_epoch}')


instr_average = 0
return_averages = ["NULL"]

#return_averages[0] = "NULL"
#for i in range(1, 500):
#fh = open("epoch_average_for_1.txt", "w")


instr = requests.get('http://egchallenge.tech/marketdata/instrument/' + str(1)).json()
if instr[len(instr)-1]['is_trading']:
    for i in range (1, len(instr)):
        instr_average += instr[i]['epoch_return']
instr_average = instr_average / (len(instr)-1)
print(instr_average)
