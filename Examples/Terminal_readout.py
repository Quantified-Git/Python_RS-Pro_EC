import RS_EC

meter = RS_EC.ecMeter('COM6')

while 1:
    try:
        res = meter.read()
        print(f"Upper Display: {res['upValue']} {res['upUnit']}, Lower Display: {res['lowValue']} {res['lowUnit']}")
    except RS_EC.SensorError:
        print("device not responding")