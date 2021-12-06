EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L SparkFun-Electromechanical:MOTOR10MM M3
U 1 1 614CBD11
P 4800 3100
F 0 "M3" H 4908 3203 45  0000 L CNN
F 1 "MOTOR10MM" H 4908 3119 45  0000 L CNN
F 2 "alexglow-footprints:bee-vibe-cu" H 4800 3350 20  0001 C CNN
F 3 "" H 4800 3100 50  0001 C CNN
F 4 "COMP-08572" H 4908 3024 60  0000 L CNN "Field4"
	1    4800 3100
	1    0    0    -1  
$EndComp
$Comp
L alexglow-symbols:powerJump J1
U 1 1 614CBF73
P 4800 2600
F 0 "J1" V 4612 2688 50  0000 L CNN
F 1 "powerJump" V 4703 2688 50  0000 L CNN
F 2 "alexglow-footprints:2-pin-power" H 4800 2600 50  0001 C CNN
F 3 "" H 4800 2600 50  0001 C CNN
	1    4800 2600
	0    1    1    0   
$EndComp
$Comp
L SparkFun-Electromechanical:MOTOR10MM M1
U 1 1 614CD090
P 3800 3100
F 0 "M1" H 3908 3203 45  0000 L CNN
F 1 "MOTOR10MM" H 3908 3119 45  0000 L CNN
F 2 "alexglow-footprints:bee-vibe-cu" H 3800 3350 20  0001 C CNN
F 3 "" H 3800 3100 50  0001 C CNN
F 4 "COMP-08572" H 3908 3024 60  0000 L CNN "Field4"
	1    3800 3100
	1    0    0    -1  
$EndComp
$Comp
L SparkFun-Electromechanical:MOTOR10MM M4
U 1 1 614CE214
P 4800 3700
F 0 "M4" H 4908 3803 45  0000 L CNN
F 1 "MOTOR10MM" H 4908 3719 45  0000 L CNN
F 2 "alexglow-footprints:bee-vibe-cu" H 4800 3950 20  0001 C CNN
F 3 "" H 4800 3700 50  0001 C CNN
F 4 "COMP-08572" H 4908 3624 60  0000 L CNN "Field4"
	1    4800 3700
	1    0    0    -1  
$EndComp
$Comp
L SparkFun-Electromechanical:MOTOR10MM M2
U 1 1 614CEE23
P 3800 3700
F 0 "M2" H 3908 3803 45  0000 L CNN
F 1 "MOTOR10MM" H 3908 3719 45  0000 L CNN
F 2 "alexglow-footprints:bee-vibe-cu" H 3800 3950 20  0001 C CNN
F 3 "" H 3800 3700 50  0001 C CNN
F 4 "COMP-08572" H 3908 3624 60  0000 L CNN "Field4"
	1    3800 3700
	1    0    0    -1  
$EndComp
Wire Wire Line
	4800 2600 4800 2800
Wire Wire Line
	4800 3300 4800 3500
Wire Wire Line
	4800 2800 3800 2800
Wire Wire Line
	3800 2800 3800 2900
Connection ~ 4800 2800
Wire Wire Line
	4800 2800 4800 2900
Wire Wire Line
	3800 3300 3800 3500
Wire Wire Line
	4800 3900 3800 3900
Wire Wire Line
	3800 3900 3500 3900
Wire Wire Line
	3500 3900 3500 2650
Wire Wire Line
	4700 2650 4700 2600
Connection ~ 3800 3900
Wire Wire Line
	3500 2650 4700 2650
$EndSCHEMATC
