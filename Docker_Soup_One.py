from bs4 import BeautifulSoup as Soup
from urllib.request import Request, urlopen
import ssl
def main():
    ssl._create_default_https_context = ssl._create_unverified_context
    url = 'https://boards.greenhouse.io/techstars57'
    req = Request(url, headers={'User-Agent': 'XYZ/3.0'})
    response = urlopen(req, timeout=20).read()
    page_soup = Soup(response, "html.parser")
    # Stock_Location_List = page_soup.find_all("div", {"class":"opening"})
    Stock_Location_List = page_soup.find_all("span")
    Location_List = [p.text for p in Stock_Location_List]
    Location_List.remove('Powered by')
    #print(Location_List)
    print(len(Location_List))
    print(type(Location_List))
    print("PAUSE")
    Stock_Date = page_soup.find_all("a")
    Date = [p.text for p in Stock_Date]
    Date.remove('Privacy Policy')
    Date.remove('\n\n')
    Date.remove('')
    #print(Date)
    print(len(Date))
    print(type(Date))

    List_One = list(Date)
    List_Two = list(Location_List)
    print(len(List_One), len(List_Two))

    #zipped = zip(List_One, List_Two)
    #print(list(zipped))
    #print(list(zipped))

    #65 65
    #Becoming 64 64????

    new_dict = dict(zip(List_One, List_Two))
    print(new_dict)
    print(len(new_dict))
    print(type(new_dict))
    #Sucessful dictionary of Locations and Job postings from techstars website

    #User_Input = print(input("Title?:"))



if __name__ == '__main__':
    main()

