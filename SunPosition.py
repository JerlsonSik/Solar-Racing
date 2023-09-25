from datetime import date
import datetime
import math
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt

def calculate_solar(year,month,day,latitude,longtitude,timezone,time):
    
    f_date = date(1900, 1, 1)   
    l_date = date(year,month,day)
    j_date = date(year,1,1)
    delta = l_date - f_date 
    julian_days = calculate_Julian_Days(month,day)
    delta_days = delta.days + 2
    time_calculate = time * ((1/60)/24)

    F = calculate_F(delta_days,time_calculate,timezone)
    G = calculate_G(F)
    I = calculate_I(G)
    J = calculate_J(G)
    K = calculate_K(G)
    L = calculate_L(J,G)
    M = calculate_M(I,L)
    N = calculate_N(J,L)
    O = calculate_O(K,N)
    P = calculate_P(M,G)
    Q = calculate_Q(G)
    R = calculate_R(Q,G)
    S = calculate_S(P,R)
    T = calculate_T(R,P)
    U = calculate_U(R)
    V = calculate_V(U,I,K,J)
    W = calculate_W(latitude,T)
    X = calculate_X(longtitude,V,timezone)
    AB = calculate_AB(time_calculate,V,longtitude,timezone)
    AC = calculate_AC(AB)
    AD = calculate_AD(latitude,T,AC)
    AE = calculate_AE(AD)
    AF = calculate_AF(AE)
    
    elevation = calculate_elevation(AE,AF)
    azimuth = calculate_azimuth(latitude,T,AC,AD)
    air_Mass = calculate_Air_Mass(elevation)
    print("Air: ",air_Mass)
    result = azimuth
    print("Delta Days: ",delta_days)
    print("Elevation: ",elevation)
    # Solar Zenith Angle
    print("Solar Zenith Angle: ",AD)
    print("Azimuth: ",result)
    print("Julians: ",julian_days)

    return elevation,azimuth,julian_days,air_Mass

def calculate_Insolation(collector_Azimuth_Angle,collector_Tilt_Angle,reflectance_Surface):
    insolation_Array = []
    
    print("Calculating with variable:")
    print("Collector Azimuth Angle: ",collector_Azimuth_Angle)
    print("Collector Tilt Angle: ",collector_Tilt_Angle)
    print("Collector Reflectance Surface: ",reflectance_Surface)
    print()
    times = [0,60,120,180,240,300,360,420,480,540,600,660,720,780,840,900,960,1020,1080,1140,1200,1260,1320,1380,1440]
    
    # for i in collector_Tilt_Angle:
    #     times_Insolation_Array = []
    #     for j in times:
    #         print("This is for angle:",i)
    #         print("The times is:",j)
    #         # 2023-8-2 on Altitude 40.424809 and Longitude -86.910500, timezone -4, time 1500
    #         elevation, azimuth, julian_Days, air_Mass = calculate_solar(2023,8,2,40.424809,-86.910500,-4,j) #TODO
    #         azimuth_angle = 180 - azimuth
    #         print()
    #         print("Elevation from Insolation:",elevation)
    #         print("Azimuth from Insolation:",azimuth)
    #         print("Julian Days from Insolation:",julian_Days)
    #         print("Azimuth Angle from Insolation:",azimuth_angle)
    #         extraterrestrial_Solar_Insolation = calculate_Extraterrestrial_Solar_Insolation(julian_Days)
    #         apparent_Extraterrestrial_Solar_Insolation = calculate_Apparent_Extraterrestrial_Solar_Insolation(julian_Days)
    #         optical_Depth = calculate_Optical_Depth(julian_Days)
    #         sky_Diffuse_Factor = calculate_Sky_Diffuse_Factor(julian_Days)
    #         sky_Beam_Radiation = calculate_Sky_Beam_Radiation(elevation,air_Mass,apparent_Extraterrestrial_Solar_Insolation,optical_Depth)
    #         angle_Of_Incidence = calculate_Angle_Of_Incidence(elevation,azimuth_angle,reflectance_Surface,i)
    #         beam_Insolation = calculate_Beam_Insolation(angle_Of_Incidence,sky_Beam_Radiation)
    #         diffuse_Radiation = calculate_Diffuse_Radiation(sky_Diffuse_Factor,sky_Beam_Radiation,i)
    #         reflected = calculate_Reflected(reflectance_Surface,sky_Beam_Radiation,elevation,sky_Diffuse_Factor,i)
    #         total_Insolation_On_Collector = calculate_Total_Insolation_On_Collector(beam_Insolation,diffuse_Radiation,reflected)
    #         print("Total Insolation On Collector: ",total_Insolation_On_Collector)
    #         times_Insolation_Array.append(total_Insolation_On_Collector)

    #     insolation_Array.append(times_Insolation_Array)

    for i in collector_Tilt_Angle:
        print("This is for angle:",i)
        elevation, azimuth, julian_Days, air_Mass = calculate_solar(2023,8,2,40.424809,-86.910500,-4,732) #TODO
        azimuth_angle = 180 - azimuth
        print()
        print("Elevation from Insolation:",elevation)
        print("Azimuth from Insolation:",azimuth)
        print("Julian Days from Insolation:",julian_Days)
        print("Azimuth Angle from Insolation:",azimuth_angle)
        extraterrestrial_Solar_Insolation = calculate_Extraterrestrial_Solar_Insolation(julian_Days)
        apparent_Extraterrestrial_Solar_Insolation = calculate_Apparent_Extraterrestrial_Solar_Insolation(julian_Days)
        optical_Depth = calculate_Optical_Depth(julian_Days)
        sky_Diffuse_Factor = calculate_Sky_Diffuse_Factor(julian_Days)
        sky_Beam_Radiation = calculate_Sky_Beam_Radiation(elevation,air_Mass,apparent_Extraterrestrial_Solar_Insolation,optical_Depth)
        angle_Of_Incidence = calculate_Angle_Of_Incidence(elevation,azimuth_angle,reflectance_Surface,i)
        beam_Insolation = calculate_Beam_Insolation(angle_Of_Incidence,sky_Beam_Radiation)
        diffuse_Radiation = calculate_Diffuse_Radiation(sky_Diffuse_Factor,sky_Beam_Radiation,i)
        reflected = calculate_Reflected(reflectance_Surface,sky_Beam_Radiation,elevation,sky_Diffuse_Factor,i)
        total_Insolation_On_Collector = calculate_Total_Insolation_On_Collector(beam_Insolation,diffuse_Radiation,reflected)
        print("Total Insolation On Collector: ",total_Insolation_On_Collector)
        insolation_Array.append(total_Insolation_On_Collector)
        
    return insolation_Array

def main():
    # latitude = 40.424809
    # longtitude = -86.910500
    # timezone = -4
    # time = 900 #This need to be minute, if time is 15:00, then the time key in should be 15*60 = 900

    # date_entry = input('Enter a date in YYYY-MM-DD format: ')
    # latitude = float(input('Enter latitdue: '))
    # longtitude = float(input('Enter longtitude: '))
    # time = int(input("Enter time: (This need to be minute, if time is 15:00, then the time key in should be 15*60 = 900)"))
    # timezone = int(input('Enter timezone: '))
    # year, month, day = map(int, date_entry.split('-'))
    # print("Date:",year, month, day)
    # print("Latitude:",latitude)
    # print("Longtitude:",longtitude)
    # print("Time:",time)
    # print("Timezone:",timezone)
    # calculate_solar(year,month,day,latitude,longtitude,timezone,time)

    # Date, time, latitude,longtitude,timezone
    # what is the power output from the specific angle 
    # Condition (Car in purdue, Specifc time:1pm) - Find the power output based on the panel angle on the car and know where get the most power 
    # changes in temperature - seperate file 
    # Power: -0.29%/ºC 

    # These are the code to calculate with array
    array_Angles = [24.606,18.531,15.468,13.371,11.765,10.441,9.29,8.25,6.84,6.342,5.42,4.491,3.017,1.984,1.007,0.151] # This use negative 90
    #array_Angles = [0.572,1.596,1.147,2.287,1.599,1.805,2.49,2.769,3.09,3.459,3.885,4.364,4.891,5.447,5.997,6.492,6.877,7.117,7.2,7.148,6.996] # This use positive 90
    #array_Angles = [0.572,1.596]
    x = calculate_Insolation(-90,array_Angles,0) # Angle to southwest is negative and to southeast is positive
    print("Insolation On Array: ",x)
    
    # data = np.random.random((12,12))
    # plt.imshow(data)
    # plt.title("W")
    # plt.show()
    # #sun angle and the solar panel angle 
    # #solar irradiance the power per unit area being apply by the sun
    # #insolation and irradiance are same 

    # #These code is plotting the sun angle graph
    # times_Main = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    # for i in x:
    #     y = i
    #     print("y",y)
    #     plt.plot(times_Main,y)
    #     # naming the x axis
    #     plt.xlabel('Insolation (kW/h)')
    #     # naming the y axis
    #     plt.ylabel('Hours (Min)')
    #     plt.title('Solar Insolation for angles')
    #     plt.show()

    # These code is for plotting the time and insolation graph
    # times_Main = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    
    # for i in range(len(array_Angles)):
    #     plt.plot(times_Main, x[i], label = "line " +  str(array_Angles[i]))
    #     # plt.plot(times_Main, x[1], label = "line 2")
    # plt.legend()
    # plt.show()

    # These code is plotting the combination graph
    # for i in x:
    #     plt.plot(times_Main, i[0], label = "line 1")
    #     plt.plot(times_Main, i[1], label = "line 2")
    #     plt.legend()
    #     plt.show()
        
def calculate_Extraterrestrial_Solar_Insolation(julian_Day):
    result = 1370 * (1 + 0.034 * math.cos(math.radians(360 * julian_Day) / 365))
    return result   

def calculate_Sky_Beam_Radiation(F18, F21, E11, E12):
    if F18 > 0:
        result = E11 * math.exp(-E12 * F21)
    else:
        result = 0
    return result

def calculate_Apparent_Extraterrestrial_Solar_Insolation(julian_Day):
    result = 1160 + 75 * math.sin(math.radians((360/365) * (julian_Day - 275)))
    return result

def calculate_Optical_Depth(julian_Day):
    result = 0.174 + 0.035 * math.sin(math.radians(360/365 * (julian_Day - 100)))
    return result

def calculate_Sky_Diffuse_Factor(julian_Day):
    result = 0.095 + 0.04 * math.sin(math.radians(360/365 * (julian_Day - 100)))
    return result

def calculate_Angle_Of_Incidence(F18, F19, L6, L7):
    result = (
        math.cos(math.radians(F18)) * 
        math.cos(math.radians(F19 - L6)) * 
        math.sin(math.radians(L7)) +
        math.sin(math.radians(F18)) * 
        math.cos(math.radians(L7))
    )
    return result

def calculate_Beam_Insolation(G30, E27):
    result = 0 if G30 < 0 else E27 * G30
    return result

def calculate_Diffuse_Radiation(E13, E27, L7):
    result = E13 * E27 * ((1 + math.cos(math.radians(L7))) / 2)
    return result

def calculate_Reflected(L8, E27, F18, E13, L7):
    result = L8 * E27 * ((math.sin(math.radians(F18)) + E13) * ((1 - math.cos(math.radians(L7))) / 2))
    return result

def calculate_Total_Insolation_On_Collector(G31, G32, G33):
    result = G31 + G32 + G33
    return result

# These are for calculating sun angle

def calculate_Julian_Days(month_name, day):
    month_offsets = {
        1: 0,
        2: 31,
        3: 59,
        4: 90,
        5: 120,
        6: 151,
        7: 181,
        8: 212,
        9: 243,
        10: 273,
        11: 304,
        12: 334
    }
    
    if month_name in month_offsets:
        result = day + month_offsets[month_name]
    else:
        result = 0
    
    return result

def calculate_F(date, time_calculate, timezone):
    result = date + 2415018.5 + time_calculate - timezone / 24
    return result

def calculate_G(F):
    result = (F - 2451545) / 36525
    return result

def calculate_I(G):
    result = (280.46646 + G * (36000.76983 + G * 0.0003032)) % 360
    return result

def calculate_J(G):
    result = 357.52911 + G * (35999.05029 - 0.0001537 * G)
    return result

def calculate_K(G):
    result = 0.016708634 - G * (0.000042037 + 0.0000001267 * G)
    return result

def calculate_L(J, G):
    result = (
        math.sin(math.radians(J)) * (1.914602 - G * (0.004817 + 0.000014 * G)) +
        math.sin(math.radians(2 * J)) * (0.019993 - 0.000101 * G) +
        math.sin(math.radians(3 * J)) * 0.000289
    )
    return result

def calculate_M(I, L):
    result = I + L
    return result

def calculate_N(J, L):
    result = J + L
    return result

def calculate_O(K, N):
    result = (1.000001018 * (1 - K * K)) / (1 + K * math.cos(math.radians(N)))
    return result

def calculate_P(M, G):
    result = M - 0.00569 - 0.00478 * math.sin(math.radians(125.04 - 1934.136 * G))
    return result

def calculate_Q(G):
    result = 23 + (26 + ((21.448 - G * (46.815 + G * (0.00059 - G * 0.001813)))) / 60) / 60
    return result

def calculate_R(Q, G):
    result = Q + 0.00256 * math.cos(math.radians(125.04 - 1934.136 * G))
    return result

def calculate_S(P, R):
    result = math.atan2(math.cos(math.radians(P)), math.cos(math.radians(R)) * math.sin(math.radians(P)))
    result = math.degrees(np.arctan(math.cos(math.radians(R)) * math.sin(math.radians(P)) / math.cos(math.radians(P))))
    return result

def calculate_T(R2, P2):
    result = math.degrees(math.asin(math.sin(math.radians(R2)) * math.sin(math.radians(P2))))
    return result

def calculate_U(R):
    result = math.tan(math.radians(R/2)) * math.tan(math.radians(R/2))
    return result

def calculate_V(U, I, K, J):
    result = (
        4 * math.degrees(U * math.sin(2 * math.radians(I)) - 
        2 * K * math.sin(math.radians(J)) + 
        4 * K * U * math.sin(math.radians(J)) * math.cos(2 * math.radians(I)) -
        0.5 * U * U * math.sin(4 * math.radians(I)) -
        1.25 * K * K * math.sin(2 * math.radians(J)))
    )
    return result

def calculate_W(latitude, T):
    result = math.degrees(math.acos(math.cos(math.radians(90.833)) / (math.cos(math.radians(latitude)) * math.cos(math.radians(T))) - math.tan(math.radians(latitude)) * math.tan(math.radians(T))))
    return result

def calculate_X(longtitude, V, timezone):
    result = (720 - 4 * longtitude - V + timezone * 60) / 1440
    return result

def calculate_AA(W):
    result = 8*W
    return result

def calculate_AB(time_calculate, V, longtitude, timezone):
    result = (time_calculate * 1440 + V + 4 * longtitude - 60 * timezone) % 1440
    return result

def calculate_AC(AB):
    if AB / 4 < 0:
        result = AB / 4 + 180
    else:
        result = AB / 4 - 180

    return result

# Solar Zenith Angle
def calculate_AD(latitude, T, AC):
    result = math.degrees(math.acos(math.sin(math.radians(latitude)) * math.sin(math.radians(T)) + math.cos(math.radians(latitude)) * math.cos(math.radians(T)) * math.cos(math.radians(AC))))
    return result

def calculate_AE(AD):
    result = 90 - AD
    return result

def calculate_AF(AE):
    if AE > 85:
        result = 0
    elif AE > 5:
        result = 58.1 / math.tan(math.radians(AE)) - 0.07 / math.pow(math.tan(math.radians(AE)), 3) + 0.000086 / math.pow(math.tan(math.radians(AE)), 5)
    elif AE > -0.575:
        result = 1735 + AE * (-518.2 + AE * (103.4 + AE * (-12.79 + AE * 0.711)))
    else:
        result = -20.772 / math.tan(math.radians(AE))
    
    return result / 3600

def calculate_elevation(AE,AF):
    return AE + AF

def calculate_azimuth(latitude, T, AC, AD):
    angle = math.degrees(math.acos(((math.sin(math.radians(latitude)) * math.cos(math.radians(AD))) - math.sin(math.radians(T))) / (math.cos(math.radians(latitude)) * math.sin(math.radians(AD)))))
    result = (angle + 180) % 360 if AC > 0 else (540 - angle) % 360
    return result

def calculate_Air_Mass(F18):
    result = abs(1 / math.sin(math.radians(F18)))
    return result

if __name__ == "__main__":
    main()