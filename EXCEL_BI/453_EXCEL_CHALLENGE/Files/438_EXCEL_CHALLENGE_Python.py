import pandas as pd

file_path = "/lakehouse/default/Files/Challenge/Excel_Challenge_438 - Resistor Value_v2.xlsx"

panda_df = pd.read_excel(file_path, usecols=[0, 1, 2, 4, 5])

color_code_dict = panda_df.set_index('Code')['Value'].to_dict()

def calculate_resistance(color_band):
    if pd.isnull(color_band):
        return None
    
    color_codes = color_band[:-2]
    multiplier_code = color_band[-2:]
    
    numeric_value = ''
    for i in range(0, len(color_codes), 2):
        color_code = color_codes[i:i+2]
        if color_code in color_code_dict:
            numeric_value += str(color_code_dict[color_code])
        else:
            return 'Invalid Color Code'
    
    if multiplier_code in color_code_dict:
        multiplier_value = color_code_dict[multiplier_code]
    else:
        return 'Invalid Multiplier Code'
    
    resistance_value = int(numeric_value) * (10 ** multiplier_value)
    
    return format_resistance(resistance_value, multiplier_value)

def format_resistance(value, multiplier):
    if value >= 1e9:
        formatted_value = f"{value / 1e9} G Ohm"
    elif value >= 1e6:
        formatted_value = f"{value / 1e6} M Ohm"
    elif value >= 1e3:
        formatted_value = f"{value / 1e3} K Ohm"
    else:
        formatted_value = f"{value} Ohm"
    
    formatted_value = formatted_value.rstrip('0').rstrip('.') if '.' in formatted_value else formatted_value
    return formatted_value

panda_df['MySolution'] = panda_df['Color Bands'].apply(calculate_resistance)

print(panda_df[['Answer Expected', 'MySolution']])
