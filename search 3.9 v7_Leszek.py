# -*- coding: utf-8 -*-

import urllib.parse
import webbrowser
import tkinter as tk

class WebPage:
    FASHION = 1
    CHILDREN = 2
    NOT_FASHION = 3
    KITCHEN = 4
    LED = 5

    def __init__(self, name, categories, variables_conjunction, address):
        self.name = name
        self.categories = categories
        self.variables_conjunction = variables_conjunction
        self.address = address
        
    def search(self, variables):
        quoted_variables = []
    
        for variable in variables:
            quoted_variables.append(urllib.parse.quote(variable))
        
        url = '%s%s' % (self.address, self.variables_conjunction.join(quoted_variables))
        print('(%s) I am opening %s ' % (self.name, url))
        webbrowser.open(url)


WEB_PAGES = [
    WebPage('H&M', [WebPage.FASHION, WebPage.NOT_FASHION, WebPage.CHILDREN, WebPage.KITCHEN],
    '+', 'https://www2.hm.com/pl_pl/search-results.html?q='),
    WebPage('Reserved', [WebPage.FASHION, WebPage.CHILDREN],
        '%20', 'https://www.reserved.com/pl/pl/?query='),
    WebPage('C&A', [WebPage.FASHION, WebPage.CHILDREN],
        '+', 'https://www.c-and-a.com/pl/pl/shop/search?q='),
    WebPage('Pepco', [WebPage.FASHION, WebPage.NOT_FASHION, WebPage.CHILDREN, WebPage.KITCHEN, WebPage.LED],
        '+', 'https://pepco.pl/?s='),
    WebPage('Sinsay', [WebPage.FASHION, WebPage.CHILDREN, WebPage.KITCHEN],
        '%20', 'https://www.sinsay.com/pl/pl/?query='),
    WebPage('Lidl', [WebPage.FASHION, WebPage.NOT_FASHION, WebPage.CHILDREN, WebPage.KITCHEN, WebPage.LED],
        '+', 'https://www.lidl-sklep.pl/q/search?q='),
    # WebPage('Home&you', [WebPage.NOT_FASHION, WebPage.KITCHEN, WebPage.LED],
    #     '+', 'https://home-you.com/pl/catalogsearch/result/?q='),
    # WebPage('Homla', [WebPage.NOT_FASHION, WebPage.KITCHEN],
    #     '+', 'https://homla.com.pl/catalogsearch/result/?q='),
    # WebPage('Ikea', [WebPage.NOT_FASHION, WebPage.KITCHEN, WebPage.LED],
    #     '%20', 'https://www.ikea.com/pl/pl/search/products/?q='),

    # WebPage('Jysk', [WebPage.NOT_FASHION, WebPage.KITCHEN, WebPage.LED],
    #     '+', 'https://jysk.pl/search?query='),
    # WebPage('Duka', [WebPage.NOT_FASHION, WebPage.KITCHEN],
    #     '%20', 'https://duka.com/pl/wyszukiwane-produkty#?q='),
    # WebPage('Oysho', [WebPage.FASHION],
    #     '+', 'https://www.oysho.com/pl/?q='),
    # WebPage('5--10--15', [WebPage.CHILDREN, WebPage.NOT_FASHION, WebPage.KITCHEN, WebPage.LED],
    #     '%20', 'https://www.51015kids.eu/products/search/'),
    # WebPage('AgataMeble', [WebPage.NOT_FASHION, WebPage.KITCHEN],
    #     '+', 'https://www.agatameble.pl/search?query%5Bquerystring%5D='),
    # WebPage('4F', [WebPage.FASHION, WebPage.NOT_FASHION],
    #     '%20', 'https://4f.com.pl/catalogsearch/result/query:'),
    # WebPage('Black Red White', [WebPage.NOT_FASHION],
    #     '%20', 'https://www.brw.pl/wyszukiwarka-zaawansowana/?query='),
    # WebPage('Coffeedesk', [WebPage.NOT_FASHION, WebPage.KITCHEN],
    #     '+', 'https://www.coffeedesk.pl/search?search='),
    # WebPage('Decathlon', [WebPage.FASHION, WebPage.NOT_FASHION],
    #     '+', 'https://www.decathlon.pl/search?Ntt='),
    # WebPage('MediaExpert', [WebPage.NOT_FASHION, WebPage.LED],
    #     '%2520', 'https://www.mediaexpert.pl/search?query[menu_item]=&query[querystring]='),
    # WebPage('Rossmann', [WebPage.NOT_FASHION, WebPage.KITCHEN],
    #     '%20', 'https://www.rossmann.pl/szukaj?Search='),
    # WebPage('Smyk', [WebPage.FASHION, WebPage.CHILDREN, WebPage.NOT_FASHION, WebPage.KITCHEN, WebPage.LED],
    #     '%20', 'https://www.smyk.com/search?q='),
    # WebPage('Triumph', [WebPage.FASHION],
    #     '+', 'https://pl.triumph.com/on/demandware.store/Sites-PL-Site/pl_PL/Search-Show?q='),
    # WebPage('Wittchen', [WebPage.NOT_FASHION],
    #     '%20', 'https://www.wittchen.com/szukaj#?q='),
    # WebPage('Zara', [WebPage.FASHION],
    #     '%20', 'https://www.zara.com/pl/pl/search?searchTerm='),
    # WebPage('ZaraHome', [WebPage.NOT_FASHION, WebPage.KITCHEN, WebPage.LED],
    #     '%20', 'https://www.zarahome.com/pl/search.html?term='),
]

window = tk.Tk()

tk.Label(window, text = 'Wpisz nazwę produktu').place(x = 50, y = 15)
variables = tk.Text(window)
variables.place(x = 50, y = 50, width = 500, height = 200)

tk.Label(window, text = 'W jakich sklepach szukać?').place(x = 50, y = 270)
shopCategory = tk.IntVar()
button = tk.Radiobutton(window,text = 'Wszystkie', value = 0, variable = shopCategory)
button.place(x = 50, y = 300)
button.select()
button = tk.Radiobutton(window,text = 'Moda', value = WebPage.FASHION, variable = shopCategory)
button.place(x = 50, y = 330)
button = tk.Radiobutton(window,text = 'Dzieci', value = WebPage.CHILDREN, variable = shopCategory)
button.place(x = 50, y = 360)
button = tk.Radiobutton(window,text = 'Kuchnia, jadalnia', value = WebPage.KITCHEN, variable = shopCategory)
button.place(x = 50, y = 390)
button = tk.Radiobutton(window,text = 'Nie modowe', value = WebPage.NOT_FASHION, variable = shopCategory)
button.place(x = 50, y = 420)
button = tk.Radiobutton(window,text = 'LED', value = WebPage.LED, variable = shopCategory)
button.place(x = 50, y = 450)

def searchClicked():
    print('searchClicked()')
    separated_variables = variables.get("1.0", tk.END).split()
    
    for i in range(len(separated_variables)):
        separated_variables[i] = separated_variables[i].encode('utf-8')

    for page in WEB_PAGES:
        if shopCategory.get() == 0:
            page.search(separated_variables)
        elif shopCategory.get() in page.categories:
            page.search(separated_variables)

window.title('Wyszukiwanie produktów. Copyright by MarketSide')
window.geometry('600x600')

button = tk.Button(window, text = "Szukaj", command = searchClicked)
button.place(x = 50, y = 500)

window.mainloop()
