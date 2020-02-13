# LoRa_Irrigation
Simplest LoRa Nodes/Gateway/Software for measuring and contriling soil moisture for farmers

LoRa Irrigation
This projects measures the huminity of soil, and water used to
keep certain level of moinsture. User can set the humidity thresholds
and hour where valves should be open.

This projects uses LoRa in a master-slave arquitecture to 
send data with a prestablished frecuency and it also has small
reception windows in order to save battery as much as possible.


There will be two kinds of nodes: Valves and Sensors

Data will be stored in a Postgres DataBase

DataBase Structure:

DB_LoRaIrrigation:

    SensorNode:
        id
        Location
        Name
        CurrentValue
        BatteryValue
        PanelValue
        TxFrecuency
        TxSlot
        RxWindow

    SensorData
        id
        DateTime
        SensorNode
        SensorValue
        BatteryValue

    ValveNode
        id
        Location
        Status(open/close)
        VolumeCount
        BatteryValue
        PanelValue
        TxFrecuency
        TxSlot
        RxWindow
        OpenValue
        CloseValue

    ValveData
        id
        DateTime
        Status
        VolumeCountValue
        BatteryValue
