import pandas as pd

# Ethiopic to Latin transliteration map (partial, can be extended)
ethiopic_map = {
    # Ha series
    'ሀ':'he','ሁ':'hu','ሂ':'hi','ሃ':'ha','ሄ':'he','ህ':'h','ሆ':'ho',
    # La
    'ለ':'le','ሉ':'lu','ሊ':'li','ላ':'la','ሌ':'le','ል':'l','ሎ':'lo',
    # Ḩa (H with dot)
    'ሐ':'ḥe','ሑ':'ḥu','ሒ':'ḥi','ሓ':'ḥa','ሔ':'ḥe','ሕ':'ḥ','ሖ':'ḥo',
    # Ma
    'መ':'me','ሙ':'mu','ሚ':'mi','ማ':'ma','ሜ':'me','ም':'m','ሞ':'mo',
    # Ṣa (śa, old)
    'ሠ':'śe','ሡ':'śu','ሢ':'śi','ሣ':'śa','ሤ':'śe','ሥ':'ś','ሦ':'śo',
    # Ra
    'ረ':'re','ሩ':'ru','ሪ':'ri','ራ':'ra','ሬ':'re','ር':'r','ሮ':'ro',
    # Sa
    'ሰ':'se','ሱ':'su','ሲ':'si','ሳ':'sa','ሴ':'se','ስ':'s','ሶ':'so',
    # Sha
    'ሸ':'she','ሹ':'shu','ሺ':'shi','ሻ':'sha','ሼ':'she','ሽ':'sh','ሾ':'sho',
    # Qa
    'ቀ':'qe','ቁ':'qu','ቂ':'qi','ቃ':'qa','ቄ':'qe','ቅ':'q','ቆ':'qo',
	# Qa
    'ቐ':'qe','ቑ':'qu','ቒ':'qi','ቓ':'qa','ቔ':'qe','ቕ':'q','ቖ':'qo',
    # Qwa (labialized)
    'ቈ':'qwe','ቊ':'qwi','ቋ':'qwa','ቌ':'qwe','ቍ':'qw','቎':'qwo',
    # Ba
    'በ':'be','ቡ':'bu','ቢ':'bi','ባ':'ba','ቤ':'be','ብ':'b','ቦ':'bo',
    # Va (rare, loanwords)
    'ቨ':'ve','ቩ':'vu','ቪ':'vi','ቫ':'va','ቬ':'ve','ቭ':'v','ቮ':'vo',
    # Ta
    'ተ':'te','ቱ':'tu','ቲ':'ti','ታ':'ta','ቴ':'te','ት':'t','ቶ':'to',
    # Ca (cha)
    'ቸ':'che','ቹ':'chu','ቺ':'chi','ቻ':'cha','ቼ':'che','ች':'ch','ቾ':'cho',
    # Ha (glottal)
    'ኀ':'he','ኁ':'hu','ኂ':'hi','ኃ':'ha','ኄ':'he','ኅ':'h','ኆ':'ho',
	# Ne (glottal)
    'ነ':'ne','ኑ':'nu','ኒ':'ni','ና':'na','ኔ':'ne','ን':'n','ኖ':'no',
	# Ha (glottal)
    'ኘ':'gne','ኙ':'gnu','ኚ':'gni','ኛ':'gna','ኜ':'gne','ኝ':'gn','ኞ':'gno',
    # ʾA (Alef)
    'አ':'a','ኡ':'u','ኢ':'i','ኣ':'a','ኤ':'e','እ':'e','ኦ':'o',
	# ʾA (Alef)
    'ዐ':'a','ዑ':'u','ዒ':'i','ዓ':'a','ዔ':'e','ዕ':'e','ዖ':'o',
    # Ka
    'ከ':'ke','ኩ':'ku','ኪ':'ki','ካ':'ka','ኬ':'ke','ክ':'k','ኮ':'ko',
	# Ke
    'ኸ':'ke','ኹ':'ku','ኺ':'ki','ኻ':'ka','ኼ':'ke','ኽ':'k','ኾ':'ko',
    # Kwa
    'ኰ':'kwe','ኲ':'kwi','ኳ':'kwa','ኴ':'kwe','ኵ':'kw','኶':'kwo',
    # Wa
    'ወ':'we','ዉ':'wu','ዊ':'wi','ዋ':'wa','ዌ':'we','ው':'w','ዎ':'wo',
    # Za
    'ዘ':'ze','ዙ':'zu','ዚ':'zi','ዛ':'za','ዜ':'ze','ዝ':'z','ዞ':'zo',
    # Ža (Zhe)
    'ዠ':'že','ዡ':'žu','ዢ':'ži','ዣ':'ža','ዤ':'že','ዥ':'ž','ዦ':'žo',
    # Ya
    'የ':'ye','ዩ':'yu','ዪ':'yi','ያ':'ya','ዬ':'ye','ይ':'y','ዮ':'yo',
    # Da
    'ደ':'de','ዱ':'du','ዲ':'di','ዳ':'da','ዴ':'de','ድ':'d','ዶ':'do',
    # Ja
    'ጀ':'je','ጁ':'ju','ጂ':'ji','ጃ':'ja','ጄ':'je','ጅ':'j','ጆ':'jo',
    # Ga
    'ገ':'ge','ጉ':'gu','ጊ':'gi','ጋ':'ga','ጌ':'ge','ግ':'g','ጎ':'go',
	'ጐ':'go',
    # Ṭa
    'ጠ':'ṭe','ጡ':'ṭu','ጢ':'ṭi','ጣ':'ṭa','ጤ':'ṭe','ጥ':'ṭ','ጦ':'ṭo',
    # Ṭʷa
    'ጨ':'che','ጩ':'chu','ጪ':'chi','ጫ':'cha','ጬ':'che','ጭ':'ch','ጮ':'cho',
    # Pa
    'ጰ':'pe','ጱ':'pu','ጲ':'pi','ጳ':'pa','ጴ':'pe','ጵ':'p','ጶ':'po',
    # Ṣa
    'ጸ':'tṣe','ጹ':'tṣu','ጺ':'tṣi','ጻ':'tṣa','ጼ':'tṣe','ጽ':'tṣ','ጾ':'tṣo',
    # Ṭsa (ts’a)
    'ፀ':'tse','ፁ':'tsu','ፂ':'tsi','ፃ':'tsa','ፄ':'tse','ፅ':'ts','ፆ':'tso',
    # Fa
    'ፈ':'fe','ፉ':'fu','ፊ':'fi','ፋ':'fa','ፌ':'fe','ፍ':'f','ፎ':'fo',
    # Pe (second)
    'ፐ':'pe','ፑ':'pu','ፒ':'pi','ፓ':'pa','ፔ':'pe','ፕ':'p','ፖ':'po',

}

def transliterate(text: str) -> str:
    """Convert Ethiopic text to Latin using the mapping"""
    return ''.join(ethiopic_map.get(ch, ch) for ch in str(text))

def process_excel(input_file, output_file, sheet_name="South East", target_column="farmer_name"):
    # Load the Excel file
    df = pd.read_excel(input_file, sheet_name=sheet_name)

    # Apply transliteration to the chosen column
    df[f"{target_column}_transliterated"] = df[target_column].apply(transliterate)

    # Save the updated Excel
    df.to_excel(output_file, sheet_name=sheet_name, index=False)
    print(f"✅ File saved as: {output_file}")


# Example usage
process_excel("Book1.xlsx", "Book1_transliterated.xlsx")
