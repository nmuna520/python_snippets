obj_test = {
    'Obj1':'1.21cm',
    'Ob2':'2.21cm',
    'Obj3':'1.21cm',
    'Obj4':'0.98cm',
    'Obj5':'1.01cm',
}

other_obj = {
    k: float(v.strip('cm'))
      for k, v in obj_test.items()
}

max_value = max(other_obj.values())

who = [k for k, v in other_obj.items() if v == max_value]