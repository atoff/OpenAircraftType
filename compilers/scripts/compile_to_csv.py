import os,csv,configparser

outputcsv = "../build/ALL_DATA.csv";
readdir = "../src";
man_cols={"NAME":"manufacturer_name","COMPANY":"manufacturer_company"}
type_cols={"MODEL":"model","ICAO":"icao","CLASS":"class","WAKE":"wake","ENG_TYPE":"engine_type","ENG_NUM":"engine_number","ENG_NAME":"engine_name","ENG_MAN":"engine_manufacturer","ENG_MODEL":"engine_model","ENG_THRUST":"engine_thrust","LENGTH":"length","WINGSPAN":"wingspan","TAIL_HEIGHT":"tail_height","RANGE":"range","CEILING":"ceiling","MAX_SPEED":"max_speed","PAX_CAP":"passenger_capacity"}
varient_cols={"BASE_MODEL":"base_model"}
cols={**man_cols, **{"is_varient":'is_varient'}, **type_cols, **varient_cols}
if os.path.exists(outputcsv):
    os.remove(outputcsv)
csv_file = open(outputcsv,'w', newline='')
writer = csv.writer(csv_file);
writer.writerow(cols.values())
# Iterate Manufacturers
for manu in os.listdir(readdir):
    config = configparser.ConfigParser()
    conf_file = open(readdir+"/"+manu+"/manufacturer.txt", 'r')
    config.read_string('[MANUFACTURER]\n'+conf_file.read())
    config = config['MANUFACTURER']
    man_insert = [config.get('name'),config.get('company')]
    print(config.get('name'))
    # Iterate Types
    for type in os.listdir(readdir+"/"+manu):
        row = []
        if os.path.isfile(os.path.join(readdir+"/"+manu, type)):
            continue
        model_config = configparser.ConfigParser()
        model_conf_file = open(readdir+"/"+manu+"/"+type+"/"+type+".txt", 'r')
        model_config.read_string('[MODEL]\n'+model_conf_file.read().replace('%','%%'))
        model_config = model_config['MODEL']
        model_insert =type_cols
        for key in type_cols:
            model_insert[key] = model_config.get(key, '')
        writer.writerow(man_insert+[0]+list(model_insert.values()))
        # Iterate Varients
        if os.path.exists(readdir+"/"+manu+"/"+type+"/Varients"):
            for varient in os.listdir(readdir+"/"+manu+"/"+type+"/Varients"):
                if os.path.isdir(readdir+"/"+manu+"/"+type+"/Varients/"+varient):
                    continue
                varient_config = configparser.ConfigParser()
                varient_config.optionxform = str
                varient_conf_file = open(readdir+"/"+manu+"/"+type+"/Varients/"+varient, 'r')
                varient_config.read_string('[VARIENT]\n'+varient_conf_file.read())
                varient_config = varient_config['VARIENT']
                #varient_insert = varient_cols
                #for key in varient_cols:
                #    varient_insert[key] = varient_config.get(key, '')
                varient_insert2 = model_insert.copy()
                for key in varient_config:
                    if key in varient_insert2:
                        varient_insert2[key] = varient_config[key]
                writer.writerow(man_insert+[1]+list({**varient_insert2, **{'BASE_MODEL':model_config.get('MODEL', type)}}.values()))
                varient_conf_file.close()
            
        model_conf_file.close()
    conf_file.close()
    print('-----------')
    
csv_file.close()

