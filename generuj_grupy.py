import pandas as pd
import numpy as np

def generuj(file):
    df = pd.read_excel(file)
    #uproszczenie nazw
    df.rename(columns={
        'Nazwa kampanii': 'kampania',
        'Nazwa grupy reklam': 'grupa',
        'Tytuł klikniętej oferty': 'tytuł',
        'Numer klikniętej oferty': 'id',
        'Wyświetlenia': 'wyswietlenia',
        'Kliknięcia': 'klikniecia',
        'Zainteresowanie': 'z',
        'CPC(PLN)': 'cpc',
        'CTR': 'ctr',
        'Koszt(PLN)': 'koszt',
        'Zwrot z inwestycji(PLN)': 'zwrot',
        'Liczba sprzedanych sztuk': 'sztuki',
        'Wartość sprzedaży(PLN)': 'sprzedaz'     
    }, inplace=True)

    #dodanie ważnego współczynika
    df['cts'] = df.klikniecia / df.sztuki
    df.replace([np.inf, -np.inf, np.nan], 0, inplace=True)
    df.head()
    ### G1
    # "oferty z dobryą konwersją ale małą ilością sprzedaży np duży zwrot i małe wartości cts = kliknięcia/sprzedane sztuki(sztuki)"
    #ustawienie współczyników selekcji grupy 1
    CTS = 20  #mijszjszy równy 
    ZWROT = 5 #większy niż
    #mniej ważne współczyniki
    sprzedane_sztuki = 10
    ilość_unikalnych_id = 60
    #czyli oferty będą miały współczynik CTS =< 20 zwrot większy niż 5 i liczba sprzedanych sztuk mniejsza równa 10 i liczba unikalnych ofert nie przekroczy 100
    g1=df.copy()
    g1 = g1[(df.cts > 1) & (df.cts <= CTS)][(df.sztuki <= sprzedane_sztuki)][(df.zwrot > ZWROT)]  
    g1.sort_values(by=['zwrot'], ascending=False, inplace=True)
    g1 = g1.drop_duplicates(subset='id') #usunięcie duplikatów z gorszym zwrotem
    g1 = g1.iloc[:ilość_unikalnych_id]
    g1.reset_index(drop=True, inplace=True)

    #ustawienie współczyników selekcji grupy 2
    CTS = 20 #większe 
    ZWROT = 6 # mniejszy niż
    #mniej ważne współczyniki
    sprzedane_sztuki = 10 #mniej niż 
    ilość_unikalnych_id = 30

    g2 = df.copy()
    g2 = g2[(df.cts > 20)][(df.sztuki <= sprzedane_sztuki)][(df.zwrot < ZWROT)]  
    g2.sort_values(by=['zwrot'], ascending=True, inplace=True)
    g2 = g2.drop_duplicates(subset='id')#usunięcie duplikatów z lepszym zwrotem
    g2 = g2.iloc[:ilość_unikalnych_id]
    g2.reset_index(drop=True, inplace=True)
    # g2.info()
    # g2.head(10)

    #dodanie linku do sprawdzenia oferty
    g2['link'] = g2.apply(lambda row: f"https://allegro.pl/show_item.php?item={row.id}", axis=1)
    #g2.head(3)
    return [g1,g2]
