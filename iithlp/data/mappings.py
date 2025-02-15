import pandas as pd
from indic_transliteration import sanscript
from indic_transliteration.sanscript import SchemeMap, SCHEMES

def create_mapping_dataframe():
    # Define the scripts we want to map
    scripts = {
        'bengali': sanscript.BENGALI,
        'gujarati': sanscript.GUJARATI,
        'kannada': sanscript.KANNADA,
        'oriya': sanscript.ORIYA,
        'gurmukhi': sanscript.GURMUKHI  # Punjabi script
    }
    
    existing_df = pd.read_csv('mappings.csv')
    
    new_mappings = {'Roman': existing_df['Roman']}
    
    for script_name, script_code in scripts.items():
        try:
            new_column = []
            for _, row in existing_df.iterrows():
                if pd.isna(row['Devanagari']):
                    new_column.append('')
                else:
                    try:
                        converted = sanscript.transliterate(
                            row['Devanagari'],
                            sanscript.DEVANAGARI,
                            script_code
                        )
                        new_column.append(converted)
                    except:
                        new_column.append('')
            
            new_mappings[script_name.title()] = new_column
            
        except Exception as e:
            print(f"Error processing {script_name}: {str(e)}")
    
    new_df = pd.DataFrame(new_mappings)
    
    new_df.to_csv('extended_mappings.csv', index=False)
    return new_df

if __name__ == "__main__":
    df = create_mapping_dataframe()
    print("New mappings generated in 'extended_mappings.csv'")
    print("\nPreview of the first few rows:")
    print(df.head())