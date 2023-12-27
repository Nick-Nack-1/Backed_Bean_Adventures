<?xml version="1.0" encoding="UTF-8"?>
<tileset version="1.10" tiledversion="1.10.2" name="More" tilewidth="16" tileheight="16" tilecount="600" columns="40">
 <image source="mines_of_sharega.png" width="640" height="240"/>
 <tile id="0">
  <properties>
   <property name="Will_kill" type="bool" value="true"/>
  </properties>
 </tile>
 <tile id="1">
  <properties>
   <property name="Will_kill" type="bool" value="true"/>
  </properties>
 </tile>
 <tile id="2">
  <properties>
   <property name="Will_kill" type="bool" value="true"/>
  </properties>
 </tile>
 <tile id="3">
  <properties>
   <property name="Will_kill" type="bool" value="true"/>
  </properties>
 </tile>
 <tile id="4" type="Death">
  <properties>
   <property name="Will_kill" type="bool" value="true"/>
   <property name="_" value="Animation_placeholder"/>
  </properties>
 </tile>
 <tile id="160" type="Red_lever">
  <properties>
   <property name="Can_Interact" type="bool" value="true"/>
   <property name="On" type="bool" value="false"/>
  </properties>
  <animation>
   <frame tileid="160" duration="2000"/>
   <frame tileid="161" duration="2000"/>
  </animation>
 </tile>
 <tile id="161" type="Red_lever">
  <properties>
   <property name="Can_Interact" type="bool" value="true"/>
  </properties>
 </tile>
 <tile id="162" type="Green_lever">
  <properties>
   <property name="Can_Interact" type="bool" value="true"/>
   <property name="On" type="bool" value="false"/>
  </properties>
  <animation>
   <frame tileid="162" duration="2000"/>
   <frame tileid="163" duration="2000"/>
  </animation>
 </tile>
 <tile id="163" type="Green_lever">
  <properties>
   <property name="Can_Interact" type="bool" value="true"/>
  </properties>
 </tile>
 <tile id="164" type="Blue_lever">
  <properties>
   <property name="Can_Interact" type="bool" value="true"/>
   <property name="On" type="bool" value="false"/>
  </properties>
  <animation>
   <frame tileid="164" duration="2000"/>
   <frame tileid="165" duration="2000"/>
  </animation>
 </tile>
 <tile id="165" type="Blue_lever">
  <properties>
   <property name="Can_Interact" type="bool" value="true"/>
  </properties>
 </tile>
 <tile id="166">
  <properties>
   <property name="Can_Interact" type="bool" value="true"/>
  </properties>
 </tile>
 <tile id="240" type="Red_door">
  <properties>
   <property name="Open" type="bool" value="false"/>
  </properties>
  <animation>
   <frame tileid="240" duration="2000"/>
   <frame tileid="243" duration="2000"/>
  </animation>
 </tile>
 <tile id="241" type="Green_door">
  <properties>
   <property name="Open" type="bool" value="false"/>
  </properties>
  <animation>
   <frame tileid="241" duration="2000"/>
   <frame tileid="283" duration="2000"/>
  </animation>
 </tile>
 <tile id="242" type="Blue_door">
  <properties>
   <property name="Open" type="bool" value="false"/>
  </properties>
  <animation>
   <frame tileid="242" duration="2000"/>
   <frame tileid="243" duration="2000"/>
  </animation>
 </tile>
 <tile id="280" type="Red_door">
  <properties>
   <property name="Open" type="bool" value="false"/>
  </properties>
  <animation>
   <frame tileid="280" duration="2000"/>
   <frame tileid="244" duration="2000"/>
  </animation>
 </tile>
 <tile id="281" type="Green_door">
  <properties>
   <property name="Open" type="bool" value="false"/>
  </properties>
  <animation>
   <frame tileid="281" duration="2000"/>
   <frame tileid="283" duration="2000"/>
  </animation>
 </tile>
 <tile id="282" type="Blue_door">
  <properties>
   <property name="Open" type="bool" value="false"/>
  </properties>
  <animation>
   <frame tileid="282" duration="2000"/>
   <frame tileid="283" duration="2000"/>
  </animation>
 </tile>
</tileset>
