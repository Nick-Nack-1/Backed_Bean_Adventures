<?xml version="1.0" encoding="UTF-8"?>
<tileset version="1.10" tiledversion="1.10.2" name="Conveyors" tilewidth="16" tileheight="16" tilecount="20" columns="5">
 <image source="../Images/Conveyor.png" width="80" height="64"/>
 <tile id="0" type="Conveyor">
  <animation>
   <frame tileid="0" duration="10"/>
   <frame tileid="5" duration="10"/>
   <frame tileid="10" duration="10"/>
   <frame tileid="15" duration="10"/>
  </animation>
 </tile>
 <tile id="1" type="Conveyor">
  <animation>
   <frame tileid="1" duration="10"/>
   <frame tileid="6" duration="10"/>
   <frame tileid="11" duration="10"/>
   <frame tileid="16" duration="10"/>
  </animation>
 </tile>
 <tile id="2" type="Conveyor">
  <animation>
   <frame tileid="2" duration="10"/>
   <frame tileid="7" duration="10"/>
   <frame tileid="12" duration="10"/>
   <frame tileid="17" duration="10"/>
  </animation>
 </tile>
 <tile id="3" type="Conveyor">
  <animation>
   <frame tileid="3" duration="3"/>
   <frame tileid="8" duration="3"/>
   <frame tileid="13" duration="3"/>
   <frame tileid="18" duration="3"/>
  </animation>
 </tile>
 <tile id="4">
  <properties>
   <property name="move_dir" type="int" value="-1"/>
  </properties>
 </tile>
 <tile id="5" type="Conveyor">
  <animation>
   <frame tileid="15" duration="6"/>
   <frame tileid="10" duration="6"/>
   <frame tileid="5" duration="6"/>
   <frame tileid="0" duration="6"/>
  </animation>
 </tile>
 <tile id="6" type="Conveyor">
  <animation>
   <frame tileid="16" duration="6"/>
   <frame tileid="11" duration="6"/>
   <frame tileid="6" duration="6"/>
   <frame tileid="1" duration="6"/>
  </animation>
 </tile>
 <tile id="7" type="Conveyor">
  <animation>
   <frame tileid="17" duration="6"/>
   <frame tileid="12" duration="6"/>
   <frame tileid="7" duration="6"/>
   <frame tileid="2" duration="6"/>
  </animation>
 </tile>
 <tile id="8" type="Conveyor">
  <animation>
   <frame tileid="18" duration="6"/>
   <frame tileid="13" duration="6"/>
   <frame tileid="8" duration="6"/>
   <frame tileid="3" duration="6"/>
  </animation>
 </tile>
 <tile id="9">
  <properties>
   <property name="move_dir" type="int" value="1"/>
  </properties>
 </tile>
</tileset>
