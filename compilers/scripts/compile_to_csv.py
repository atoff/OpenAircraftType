import os,csv,configparser

output_csv = "../build/ALL_DATA.csv"
read_dir = "../src"

man_cols = {
    "NAME": "manufacturer_name",
    "COMPANY": "manufacturer_company"
}

type_cols = {
    "MODEL": "model",
    "ICAO": "icao",
    "CLASS": "class",
    "WAKE": "wake",
    "ENG_TYPE": "engine_type",
    "ENG_NUM": "engine_number",
    "ENG_NAME": "engine_name",
    "ENG_MAN": "engine_manufacturer",
    "ENG_MODEL": "engine_model",
    "ENG_THRUST": "engine_thrust",
    "LENGTH": "length",
    "WINGSPAN": "wingspan",
    "TAIL_HEIGHT": "tail_height",
    "RANGE": "range",
    "CEILING": "ceiling",
    "MAX_SPEED": "max_speed",
    "PAX_CAP": "passenger_capacity",
    "REMARKS": "remarks"
}

variant_cols = {"BASE_MODEL": "base_model"}

cols = {**man_cols, **{"is_variant": 'is_variant'}, **type_cols, **variant_cols}

if os.path.exists(output_csv):
    os.remove(output_csv)

csv_file = open(output_csv, 'w', newline='')

writer = csv.writer(csv_file)
writer.writerow(cols.values()) # write titles header row

for group_dir in os.listdir(read_dir): # iterate high-level groups, like A, B, C etc.
    
    for manufacturer in os.listdir(os.path.join(read_dir, group_dir)): # Iterate Manufacturers
        config = configparser.ConfigParser()

        manufacturer_dir = os.path.join(read_dir, group_dir, manufacturer)

        with open(os.path.join(manufacturer_dir, "manufacturer.txt"), 'r') as file:
            config.read_string('[MANUFACTURER]\n' + file.read())
        
        config = config['MANUFACTURER']
        man_insert = [config.get('name'), config.get('company')]
        print(config.get('name'))

        # Iterate Types
        for aircraft_type in os.listdir(manufacturer_dir):

            if os.path.isfile(os.path.join(manufacturer_dir, aircraft_type)):
                continue
            model_config = configparser.ConfigParser()

            with open(os.path.join(manufacturer_dir, aircraft_type, aircraft_type + ".txt"), 'r') as file:
                model_config.read_string('[MODEL]\n' + file.read().replace('%','%%'))
        
            model_config = model_config['MODEL']
            model_insert = type_cols

            for key in type_cols:
                model_insert[key] = model_config.get(key, '')

            writer.writerow(man_insert + [0] + list(model_insert.values()))
            
            # Iterate Variants
            variants_dir = os.path.join(manufacturer_dir, aircraft_type, "Variants")
            if os.path.exists(variants_dir):
                for variant in os.listdir(variants_dir):
                    if os.path.isdir(os.path.join(variants_dir, variant)):
                        continue

                    variant_config = configparser.ConfigParser()
                    variant_config.optionxform = str
                    
                    with open(os.path.join(variants_dir, variant), 'r') as file:
                        variant_config.read_string('[VARIANT]\n' + file.read())

                    variant_config = variant_config['VARIANT']

                    variant_insert = model_insert.copy()
                    for key in variant_config:
                        if key in variant_insert:
                            variant_insert[key] = variant_config[key]
                    writer.writerow(man_insert + [1] + list({**variant_insert, **{'BASE_MODEL': model_config.get('MODEL', aircraft_type)}}.values()))
        print('-----------')

csv_file.close()