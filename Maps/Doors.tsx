<?xml version="1.0" encoding="UTF-8"?>
<tileset version="1.10" tiledversion="1.10.2" name="Doors" tilewidth="16" tileheight="16" tilecount="12" columns="6">
 <image source="../Images/Doors.png" width="96" height="32"/>
 <tile id="1" type="Blue_door">
  <properties>
   <property name="Open" type="bool" value="false"/>
  </properties>
  <animation>
   <frame tileid="1" duration="2000"/>
   <frame tileid="0" duration="2000"/>
  </animation>
 </tile>
 <tile id="0"/>
 <tile id="3" type="Red_door">
  <properties>
   <property name="Open" type="bool" value="false"/>
  </properties>
  <animation>
   <frame tileid="3" duration="2000"/>
   <frame tileid="2" duration="2000"/>
  </animation>
 </tile>
 <tile id="2"/>
 <tile id="5" type="Green_door">
  <properties>
   <property name="Open" type="bool" value="false"/>
  </properties>
  <animation>
   <frame tileid="5" duration="2000"/>
   <frame tileid="4" duration="2000"/>
  </animation>
 </tile>
 <tile id="4"/>
 <tile id="7" type="Blue_door">
  <properties>
   <property name="Open" type="bool" value="false"/>
  </properties>
  <animation>
   <frame tileid="7" duration="2000"/>
   <frame tileid="6" duration="2000"/>
  </animation>
 </tile>
 <tile id="6"/>
 <tile id="9" type="Red_door">
  <properties>
   <property name="Open" type="bool" value="false"/>
  </properties>
  <animation>
   <frame tileid="9" duration="2000"/>
   <frame tileid="8" duration="2000"/>
  </animation>
 </tile>
 <tile id="8"/>
 <tile id="11" type="Green_door">
  <properties>
   <property name="Open" type="bool" value="false"/>
  </properties>
  <animation>
   <frame tileid="11" duration="2000"/>
   <frame tileid="10" duration="2000"/>
  </animation>
 </tile>
 <tile id="10"/>
</tileset>
