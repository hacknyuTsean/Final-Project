import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline


class Compaction_Test:

    def __init__(self,name,pdata=None,data1=None,data2=None,data3=None,MSUW=None,MC=None,DUW=None,ZAV=None):
        """Constructor to be used later"""
        self.name = name
        self.pdata = []
        self.data1 = []
        self.data2 = []
        self.data3 = []
        self.data4 = []
        self.MSUW = []
        self.MC = []
        self.DUW = []
        self.ZAV =[]
        print('Init complete for {}!'.format(name))

    def add_PreData(self,weight,volume,Gs):
        """This is the input for all the preliminaries in the experiment.
        weight is the of the total weight of mold and the plate
        volume is the the volume of the mold
        Gs is the specific gravity of the soil
        These are all just constant values. """
        self.pdata.append(weight)
        self.pdata.append(volume)
        self.pdata.append(Gs)
        print(self.pdata)
        print("preliminary data was added")

    def __str__(self):
         return str(self.pdata)

    def add_weightandwetSoil(self,Mdata):
        """This is the input for the total weight of the mold,
        base plate, and wet soil"""
        self.data1.append(Mdata)
        print(self.data1)
        print("data for total weight of the mold, base plate, and wet soil was added")

    def add_masscanandwetSoil(self,Wdata):
        """This is the input for the total mass of the can
        and wet soil"""
        self.data2.append(Wdata)
        print(self.data2)
        print("data for total mass of can and wet soil was added")

    def add_masscananddrySoil(self,Ddata):
        """This is the input for the total mass of the can
        and dry soil"""
        self.data3.append(Ddata)
        print(self.data3)
        print("data for total mass of the can and dry soil was added")

    def add_massmoistcan(self,Cdata):
        """This is the input for the mass of the moisture can"""
        self.data4.append(Cdata)
        print(self.data4)
        print("data for the mass of the moisture can was added")

    def cal_moistsoilUW(self):
        """This function calculates the moist soil unit weight.It is calculated
        by subtracting total weight of the mold,base plate, and wet soil by
        the total weight of the mold and base plate. Since there are multiple
        trials, there are multiple values of moisture unit weight."""
        for i in range(len(self.data1[0])):
          if i < len(self.data1[0]):
            UW = (self.data1[0][i]-self.pdata[0])/self.pdata[1]
            self.MSUW.append(UW)
        print(self.MSUW)
        print("Moist unit weight of soil was calculated")

    def cal_moistC(self):
        """This function calculates the moisture content of soil.It is calculated
        by subtracting the total mass of can and wet soil, by the total mass of
        can and dry soil, and divided altogether by the subtraction between
        the total mass of can and dry soil, and the mass of moisture can.
        Since there are multiple trials, there are multiple values of moisture unit weight."""
        for i in range(len(self.data2[0])):
          if i < len(self.data2[0]):
            mc = (self.data2[0][i]-self.data3[0][i])/(self.data3[0][i]-self.data4[0][i])*100
            self.MC.append(mc)
        print(self.MC)
        print("Moisture content of soil was calculated")

    def cal_dryUW(self):
        """This function calculates the dry unit weight of soil.It is calculated
        by dividing the moist soil unit weight by the sum of one and moisture content,
        with moisture content in regular form instead of in percentage. Since there
        are multiple trials, there are multiple values of moisture unit weight."""
        for i in range(len(self.MC)):
          if i<len(self.MC):
            duw = self.MSUW[i]/(1+(self.MC[i]/100))
            self.DUW.append(duw)
        print(self.DUW)
        print("Dry unit weight of soil was calculated")

    def cal_zav(self):
        """This function calculates the Zero-Air-Void unit weight of soil.It is calculated
        by dividing the specific weight of water by the sum of moisture content in regular
        form instead of in percentage, and the reciprocal of soil specific gravity. Since
        there are multiple trials, there are multiple values of moisture unit weight."""
        for i in range(len(self.MC)):
          if i<len(self.MC):
            zav = 62.4/((self.MC[i]/100)+(1/self.pdata[2]))
            self.ZAV.append(zav)
        print(self.ZAV)
        print("Zero-Air-Void unit weight of soil was calculated")

    def draw_UWvsMC(self):
      """Graphing ZAV unit weight vs Moisture content
      It should be on the right of the curve below"""
      fig = plt.figure()
      graph = fig.add_subplot()
      graph.plot(self.MC,self.ZAV,label="ZAV")

      """Graphing dry unit weight vs Moisture content
      It should be on the left of the curve above"""
      """The steps below makes a curve smooth instead of
      a graph with line connecting between points"""

      x_new = np.linspace(min(self.MC), max(self.MC), 300)
      spl = make_interp_spline(self.MC,self.DUW, k=3)
      graph_smooth = spl(x_new)
      plt.plot(x_new,graph_smooth,label="Dry")

      plt.ylabel('Dry Unit Weight(lb/ft^3)')
      plt.xlabel('Moisture Content (%)')
      plt.legend()
      plt.grid()
      """It also prints the maximum dry unit weight found on the graph"""
      """There is no direct method to find the max dry unit weight and Optimal
      Moisture content, because we don't have a function for this graph. We are
      just connecting points. Thus, I have added grid for better visulization.
      In a normal standard compaction test experiment, these results were obtained
      by looking at the graph directly. Thus, it is reasonable that we do the
      same in here, but there is a way to find the max dry unit weight and I have
      implemented in my code below"""
      y_max = max(graph_smooth)
      print("The soil unit weight vs Moisture content graph is drawn above")
      print("The maximum dry unit weight is",y_max,"lb/ft^3")
      plt.show()
