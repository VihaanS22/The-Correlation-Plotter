import csv
import plotly.express as px
import numpy as np

print("")
print("The Correlation Plotter")
print("")
print("You have entered the correlation graph program. Now, hope you know what correlation is. Please choose the type of report you want.")
print("")
print("As graphs")
print("As decimal result")
print("")

report = input("Enter the report type :- ")
print("")


if(report == "As graphs"):

    print("You have chosen to view graphs. Please choose the data type now.")
    print("")
    print("Percentage of a class according to increasing days. Please enter 'Marks' in the input.")
    print("")
    print("Hours of sleep in a week according to intake of coffee. Please enter 'Coffee' in the input.")
    print("")
    corr = input("Enter the report type :- ")

    if(corr == "Marks"):


        def getDataSource(datapath):

            list1 = []
            list2 = []

            with open(datapath) as file:
                row = csv.DictReader(file)
                fig = px.scatter(row, x = "Days", y = "Percentage")
                fig.show()
                
                for i in row:
                    list1.append(float(i["Percentage"]))
                    list2.append(float(i["Days"]))

            return{"x" : list1, "y" : list2}

        

        def main():
            path = "marks.csv"
            getDataSource(path)
            

        main()
        print("")
        print("Thanks for using The Correlation Plotter!")
        print("")

    if(corr == "Coffee"):


        def getDataSource(datapath):

            list1 = []
            list2 = []

            with open(datapath) as file:
                row = csv.DictReader(file)
                fig = px.scatter(row, x = "Coffee", y = "sleep")
                fig.show()
                
                for i in row:
                    list1.append(float(i["Coffee"]))
                    list2.append(float(i["sleep"]))

            return{"x" : list1, "y" : list2}

       

        def main():
            path = "coffee.csv"
            getDataSource(path)
         

        main()
        print("")
        print("Thanks for using The Correlation Plotter!")
        print("")


if(report == "As decimal result"):
    print("You have chosen to view decimal values. Please choose the data type now.")
    print("")
    print("Percentage of a class according to increasing days. Please enter 'Marks' in the input.")
    print("")
    print("Hours of sleep in a week according to intake of coffee. Please enter 'Coffee' in the input.")
    print("")
    corr = input("Enter the report type :- ")

    if(corr == "Marks"):


        def getDataSource(datapath):

            list1 = []
            list2 = []

            with open(datapath) as file:
                row = csv.DictReader(file)
                #fig = px.scatter(row, x = "Days", y = "Percentage")
                #fig.show()
                
                for i in row:
                    list1.append(float(i["Percentage"]))
                    list2.append(float(i["Days"]))

            return{"x" : list1, "y" : list2}

        def findCorr(datasource):

            corr = np.corrcoef(datasource["x"], datasource["y"])
            print("CORRELATION COEFFICIENT IS :", corr[0,1])

        def main():
            path = "marks.csv"
            source = getDataSource(path)
            findCorr(source)

        main()
        print("")
        print("Thanks for using The Correlation Plotter!")
        print("")

    if(corr == "Coffee"):


        def getDataSource(datapath):

            list1 = []
            list2 = []

            with open(datapath) as file:
                row = csv.DictReader(file)
                #fig = px.scatter(row, x = "Coffee", y = "sleep")
                #fig.show()
                
                for i in row:
                    list1.append(float(i["Coffee"]))
                    list2.append(float(i["sleep"]))

            return{"x" : list1, "y" : list2}

        def findCorr(datasource):

            corr = np.corrcoef(datasource["x"], datasource["y"])
            print("CORRELATION COEFFICIENT IS :", corr[0,1])

        def main():
            path = "coffee.csv"
            source = getDataSource(path)
            findCorr(source)

        main()
        print("")
        print("Thanks for using The Correlation Plotter!")
        print("")