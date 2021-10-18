import pysaintcoinach
import csv

realm = pysaintcoinach.ARealmReversed(r"D:\game\WeGameApps\rail_apps\ffxiv(2000340)\game", pysaintcoinach.Language.chinese_simplified)
card_sheet = realm.game_data.get_sheet('TripleTriadCardResident')
card_desc_sheet = realm.game_data.get_sheet('TripleTriadCard')
card_type_sheet = realm.game_data.get_sheet('TripleTriadCardType')
rule_sheet = realm.game_data.get_sheet('TripleTriadRule')
with open('card/card_chs.csv', 'w+', encoding='utf-8') as name_file, \
        open('card/card_main.csv', 'w+', encoding='utf-8') as main_file, \
        open('card/rule_chs.csv', 'w+', encoding='utf8') as rule_file, \
        open('card/type_chs.csv', 'w+', encoding='utf8') as type_file:
    name_csv = csv.DictWriter(name_file, lineterminator='\n', fieldnames=['cid', 'name', 'desc'])
    main_csv = csv.DictWriter(main_file, lineterminator='\n', fieldnames=['cid', 'top', 'bottom', 'left', 'right', 'rarity', 'type'])
    type_csv = csv.DictWriter(type_file, lineterminator='\n', fieldnames=['tid', 'name'])
    rule_csv = csv.DictWriter(rule_file, lineterminator='\n', fieldnames=['rid', 'name'])
    for card in card_sheet:
        if not card.key: continue
        main_csv.writerow({
            'cid': card.key,
            'top': card['Top'],
            'bottom': card['Bottom'],
            'left': card['Left'],
            'right': card['Right'],
            'rarity': card['TripleTriadCardRarity']['Stars'],
            'type': card['TripleTriadCardType'].key
        })
        name_row = card_desc_sheet[card.key]
        name_csv.writerow({
            'cid': card.key,
            'name': name_row['Name'],
            'desc': name_row['Description'],
        })
    for row in card_type_sheet:
        if not row.key: continue
        type_csv.writerow({
            'tid':row.key,
            'name': row['Name'],
        })
    for row in rule_sheet:
        if not row.key: continue
        rule_csv.writerow({
            'rid':row.key,
            'name': row['Name'],
        })
