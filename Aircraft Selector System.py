from tkinter import *
import geopy
from geopy.geocoders import Nominatim
import geopy.distance


class MyWindow:
    def __init__(self, win):
    #labels
        self.lbl1=Label(win, text='Origin')
        self.lbl2=Label(win, text='Origin Country')
        self.lbl3=Label(win, text='Destination')
        self.lbl4=Label(win, text='Destination Country')
        self.lbl5=Label(win, text='Miles Traveled')
        self.lbl6=Label(win, text='Nautical miles/hr')
        self.lbl7=Label(win, text='Time in hr')
        self.lbl8=Label(win, text= "Selected aircraft")


    #entry fields
        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t3=Entry()
        self.t4=Entry()
        self.t5=Entry()
        self.t6=Entry()
        self.t7=Entry()
        self.t8=Entry()


# origin placement
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)

        self.lbl2.place(x=400, y=50)
        self.t2.place(x=500, y=50)

#destination placement
        self.lbl3.place(x=100, y=100)
        self.t3.place(x=200, y=100)

        self.t4.place(x=500, y=100)
        self.lbl4.place(x=375, y=100)
#calculate button placement
        self.b1 = Button(win, text='Calculate Distance', command=self.Calculatemiles)
        self.b1.place(x=100, y=150)
# calculate miles placement
        self.lbl5.place(x=100, y=200)
        self.t5.place(x=200, y=200)

# nautical miles used placement
        self.lbl6.place(x=400,y=200)
        self.t6.place(x=500, y=200)
# display time
        self.lbl7.place(x=100,y=250)
        self.t7.place(x=200, y=250)
# display which aircraft
        self.lbl8.place(x=410, y=250)
        self.t8.place(x=500, y=250)
# calculate time
        self.b2= Button(win, text='Time', command=self.nmtom)
        self.b2.place(x=230, y=150)
# calculate which aircraft to use
        self.b3 = Button(win, text="Aircraft generator", command=self.selectaircarft)
        self.b3.place(x=290, y=150)

#calculatemiles function


    def Calculatemiles(self):

        geolocator = Nominatim(user_agent="my_user_agent")
        city = self.t1.get()
        country = self.t2.get()
        loc = geolocator.geocode(city + ',' + country)
        city2 = self.t3.get()
        country2 = self.t4.get()
        loc1 = geolocator.geocode(city2 + ',' + country2)
        lat1 = loc.latitude
        long1 = loc.longitude
        lat2 = loc1.latitude
        long2 = loc1.longitude

        coords_1 = (lat1, long1)
        coords_2 = (lat2, long2)

        result=geopy.distance.geodesic(coords_1, coords_2).miles
        self.t5.insert(END,str(result))

    def nmtom(self): # nm to miles then divide gallons
        nm=float(self.t6.get())
        mil= nm * 1.15078

# speed = D/T
        time=(float(self.t5.get())/mil)


        self.t7.insert(END,float(time))

    def dictionary(self):
        airarray = ['737-400', '737-500', '737-700', '737-800', '747-8', '757-200',
                    '777-200', '777-200ER', '777-200LR', '777-300ER', '767-200',
                    '767-300', '767-300ER', '787-8', '787-9', 'A300', 'A319-100',
                    'A320', 'A321-100', 'A321-231', 'A330-200', 'A330-300', 'A340-300',
                    'A340-500', 'A350-900', 'A380']
        fuelarray = [915.49295775, 845.07042254, 852.11267606, 890.84507042,
                     3380.28169014, 1169.01408451, 2140.84507042, 2334.50704225,
                     2394.36619718, 2640.84507042, 1584.50704225, 1690.14084507,
                     1739.43661972, 1725.35211268, 1971.83098592, 1679.57746479,
                     835.91549296, 855.63380282, 1015.84507042, 964.78873239,
                     1968.30985915, 2007.04225352, 2288.73239437, 2816.90140845,
                     2042.25352113, 3873.23943662]

        self.dictio = {}
        for key in airarray:
            for value in fuelarray:
                self.dictio[key] = value
                fuelarray.remove(value)
                break

    def selectaircarft(self):

        b=self.dictio
        c = float(self.t7.get())
        z={}
# iterate through dictionary
        for aircraft,gas in b.items():
            total = gas * c

            z[aircraft] = total

        werte = min(z.values())
        res = [key for key in z if z[key] == werte]

        self.t8.insert(END,str(res))



# reset the order into the smallest and print that in t8



    # write algorithm to display the least fuel used aircraft








    # printing the ans




window=Tk()
mywin=MyWindow(window)
mywin.dictionary()
window.title('AMS')
window.geometry("700x300+10+10")
window.mainloop()