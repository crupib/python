
from constants import MAP_COLS, MAP_ROWS
from models import Tile, Unit, Principle, Scenario


def make_tiles(default="plain"):
    return {(q,r): Tile(q,r,default) for q in range(MAP_COLS) for r in range(MAP_ROWS)}

def rect(tiles,q1,q2,r1,r2,terrain):
    for q in range(q1,q2+1):
        for r in range(r1,r2+1):
            if (q,r) in tiles: tiles[(q,r)].terrain=terrain

def pts(tiles,points,terrain):
    for p in points:
        if p in tiles: tiles[p].terrain=terrain

def reveal_left(tiles,max_q):
    for (q,r),t in tiles.items():
        if q<=max_q: t.revealed=True

def reveal_terrain(tiles,terrain):
    for t in tiles.values():
        if t.terrain==terrain: t.revealed=True

def finish(state,tiles,units,player,enemy,msg,deploy=7,logistics=105,enemy_morale=100):
    state.tiles=tiles; state.units=units; state.selected=None; state.turn=player; state.phase="DEPLOY"; state.message=msg
    state.assessment_points=3; state.deployment_points=deploy; state.player_morale=100; state.enemy_morale=enemy_morale; state.logistics=logistics; state.turn_number=0
    state.reset_camera()

def commander_pair(player,enemy,pname,ename):
    return [Unit(pname,player,2,8,12,4,2,1,"commander"), Unit(ename,enemy,20,8,10,3,2,1,"commander",hidden=True)]

def add_standard_units(player,enemy,theme="infantry",fast="cavalry",support="artillery"):
    return [
        Unit("Main Force",player,4,8,12,4,2,1,theme), Unit("Fast Wing",player,4,6,10,4,4,1 if fast!="aircraft" else 4,fast),
        Unit("Reserve",player,3,9,10,4,2,1,"guard"), Unit("Support Guns",player,3,10,8,3,1,3,support), Unit("Scouts",player,5,7,8,3,3,2,"skirmisher"),
        Unit("Enemy Main Force",enemy,17,8,13,4,1,1,"infantry",hidden=True), Unit("Enemy Fast Wing",enemy,18,6,10,4,3,1,fast,hidden=True),
        Unit("Enemy Reserve",enemy,18,10,11,4,2,1,"guard",hidden=True), Unit("Enemy Artillery",enemy,19,9,8,3,1,3,"artillery",hidden=True),
    ]

def setup_gaugamela(state):
    tiles=make_tiles("desert"); rect(tiles,8,17,5,10,"prepared"); rect(tiles,16,22,1,4,"rough"); rect(tiles,1,3,6,9,"supply"); pts(tiles,[(12,7),(13,7),(14,8),(15,8)],"objective"); reveal_left(tiles,7)
    units=[Unit("Alexander","Macedon",2,7,12,5,3,1,"commander"),Unit("Companion Cav","Macedon",3,6,10,4,4,1,"cavalry"),Unit("Hypaspists","Macedon",4,7,11,4,2,1,"elite infantry"),Unit("Phalanx I","Macedon",3,8,13,3,1,1,"phalanx"),Unit("Phalanx II","Macedon",4,9,13,3,1,1,"phalanx"),Unit("Agrianians","Macedon",4,6,8,3,2,2,"skirmisher"),Unit("Darius","Persia",19,7,10,2,2,1,"commander",hidden=True),Unit("Persian Center","Persia",17,7,14,3,1,1,"infantry",hidden=True),Unit("Scythed Chariots","Persia",14,7,8,6,4,1,"chariot",hidden=True),Unit("Indian Elephants","Persia",15,8,16,5,2,1,"elephant",hidden=True),Unit("Bactrian Cav","Persia",17,4,10,4,4,1,"cavalry",hidden=True),Unit("Mazaeus Cav","Persia",17,11,10,4,4,1,"cavalry",hidden=True),Unit("Persian Guard","Persia",18,8,12,4,1,1,"guard",hidden=True)]
    finish(state,tiles,units,"Macedon","Persia","Gaugamela: open plain, prepared chariot lanes, elephants, rough right flank, and exposed wings.")

def setup_normaninv(state):
    tiles=make_tiles(); rect(tiles,0,2,0,15,"sea"); rect(tiles,3,5,2,13,"beach"); rect(tiles,6,7,4,11,"supply"); rect(tiles,8,15,2,13,"bocage"); rect(tiles,16,20,1,5,"village"); rect(tiles,16,22,10,14,"rough"); rect(tiles,10,11,3,12,"river"); pts(tiles,[(10,4),(11,4),(10,10),(11,10)],"bridge"); pts(tiles,[(7,5),(7,8),(8,6),(8,10)],"road"); pts(tiles,[(17,4),(18,7),(19,10),(15,6)],"bunker"); pts(tiles,[(12,4),(13,11),(15,12)],"forest"); reveal_left(tiles,7)
    units=commander_pair("Allies","Germany","Eisenhower HQ","German Command")+[Unit("Omaha Infantry","Allies",3,7,12,4,2,1,"infantry"),Unit("Utah Infantry","Allies",3,10,12,4,2,1,"infantry"),Unit("Rangers","Allies",4,6,10,5,2,1,"infantry"),Unit("Airborne North","Allies",7,4,9,4,3,1,"paratrooper"),Unit("Airborne South","Allies",7,11,9,4,3,1,"paratrooper"),Unit("Sherman Armor","Allies",3,8,13,5,3,1,"armor"),Unit("Naval Fire Support","Allies",1,8,10,5,1,4,"naval"),Unit("Atlantic Wall Bunker","Germany",17,7,14,4,0,3,"bunker",hidden=True),Unit("Coastal Artillery","Germany",18,8,9,4,1,3,"artillery",hidden=True),Unit("Panzer Reserve","Germany",20,11,13,5,3,1,"armor",hidden=True)]
    finish(state,tiles,units,"Allies","Germany","Normandy: sea, beach sectors, bunkers, river crossings, villages, bocage, and inland reserves.",deploy=8,logistics=125)

def setup_sixdaywar(state):
    tiles=make_tiles("desert"); rect(tiles,1,3,6,9,"supply"); pts(tiles,[(13,5),(17,7),(19,10)],"airfield"); pts(tiles,[(20,6),(20,9)],"objective"); pts(tiles,[(8,6),(9,6),(10,7),(11,7),(12,8)],"road"); pts(tiles,[(10,3),(11,4),(15,12),(16,11)],"rough"); pts(tiles,[(15,6),(18,9)],"city"); reveal_left(tiles,6)
    units=commander_pair("Israel","Egypt","Israeli Command","Egyptian Command")+[Unit("Mirage Squadron","Israel",2,6,9,6,5,4,"aircraft"),Unit("Vautour Squadron","Israel",2,8,9,5,5,4,"aircraft"),Unit("7th Armored","Israel",4,7,13,5,4,1,"armor"),Unit("Paratroop Brigade","Israel",4,10,10,4,3,1,"paratrooper"),Unit("Mechanized Infantry","Israel",4,5,11,4,3,1,"mechanized"),Unit("Egyptian Airfield","Egypt",17,7,12,3,0,3,"aircraft",hidden=True),Unit("SAM Battery","Egypt",15,6,10,4,1,3,"airdefense",hidden=True),Unit("Sinai Armor","Egypt",19,10,13,5,3,1,"armor",hidden=True)]
    finish(state,tiles,units,"Israel","Egypt","Six-Day War: desert maneuver lanes, forward airfields, SAM belt, rough passes, and command objectives.",deploy=7,logistics=120)

def setup_austerlitz(state):
    tiles=make_tiles(); rect(tiles,9,14,5,8,"heights"); rect(tiles,15,22,10,15,"frozen"); rect(tiles,6,7,7,9,"village"); rect(tiles,1,3,6,10,"supply"); pts(tiles,[(8,7),(9,7),(10,7),(11,7),(12,7),(13,7)],"road"); pts(tiles,[(11,6),(12,6),(11,8),(12,8)],"objective"); reveal_left(tiles,7)
    units=commander_pair("France","Coalition","Napoleon","Tsar Alexander")+add_standard_units("France","Coalition","infantry","cavalry","artillery")
    finish(state,tiles,units,"France","Coalition","Austerlitz: Pratzen Heights, frozen ponds, villages, roads, and the deliberately weak French right.")

def setup_yorktown(state):
    tiles=make_tiles(); rect(tiles,1,4,6,10,"supply"); rect(tiles,5,8,4,12,"prepared"); rect(tiles,10,12,6,10,"city"); rect(tiles,13,16,5,11,"river"); rect(tiles,17,23,3,13,"sea"); pts(tiles,[(13,7),(14,7),(13,10),(14,10)],"bridge"); pts(tiles,[(9,7),(10,10)],"bunker"); pts(tiles,[(11,8),(12,8)],"objective"); pts(tiles,[(18,7),(19,7),(20,7),(18,8),(19,8),(20,8),(19,6),(19,9)],"blockade"); reveal_left(tiles,9); reveal_terrain(tiles,"blockade")
    units=[Unit("Washington","Allies",2,8,12,3,2,1,"commander"),Unit("Rochambeau","Allies",3,9,11,3,2,1,"commander"),Unit("Continental Infantry","Allies",4,8,12,4,2,1,"infantry"),Unit("French Infantry","Allies",5,9,12,4,2,1,"infantry"),Unit("Siege Artillery","Allies",6,8,9,5,1,3,"artillery"),Unit("Light Infantry","Allies",5,10,9,4,3,1,"skirmisher"),Unit("French Fleet Center","Allies",19,7,12,5,2,4,"naval"),Unit("French Fleet North","Allies",19,6,10,4,2,3,"naval"),Unit("French Fleet South","Allies",19,9,10,4,2,3,"naval"),Unit("Cornwallis","Britain",11,8,10,2,2,1,"commander",hidden=True),Unit("Yorktown Garrison","Britain",11,9,14,3,1,1,"infantry",hidden=True),Unit("Redoubt 9","Britain",9,7,10,4,0,3,"bunker",hidden=True),Unit("Redoubt 10","Britain",10,10,10,4,0,3,"bunker",hidden=True),Unit("British Artillery","Britain",12,8,8,4,1,3,"artillery",hidden=True),Unit("Escape Boats","Britain",16,8,8,2,2,1,"naval",hidden=True)]
    finish(state,tiles,units,"Allies","Britain","Yorktown: peninsula, siege lines, redoubts, York River, and visible French naval blockade.",deploy=7,logistics=115); state.yorktown_escape_progress=0; state.yorktown_blockade_active=True

def setup_constantinople(state):
    tiles=make_tiles(); rect(tiles,1,4,5,10,"supply"); rect(tiles,5,8,4,11,"prepared"); rect(tiles,9,10,4,11,"bunker"); rect(tiles,11,15,5,10,"city"); rect(tiles,16,23,2,13,"sea"); pts(tiles,[(10,6),(10,9),(11,7),(11,8)],"objective"); pts(tiles,[(7,7),(8,7),(9,7),(10,7)],"road"); reveal_left(tiles,9)
    units=commander_pair("Ottomans","Byzantines","Mehmed II","Constantine XI")+[Unit("Janissaries","Ottomans",4,8,13,5,2,1,"guard"),Unit("Anatolian Infantry","Ottomans",4,9,12,4,2,1,"infantry"),Unit("Great Bombard","Ottomans",6,8,10,6,1,4,"artillery"),Unit("Sappers","Ottomans",6,10,8,3,2,1,"skirmisher"),Unit("Ottoman Fleet","Ottomans",17,7,10,4,2,3,"naval"),Unit("Theodosian Walls","Byzantines",10,8,16,4,0,3,"bunker",hidden=True),Unit("Gate Defenders","Byzantines",11,8,12,4,1,1,"guard",hidden=True),Unit("Greek Fire Ships","Byzantines",17,9,9,4,2,3,"naval",hidden=True),Unit("Wall Artillery","Byzantines",10,10,8,3,0,3,"artillery",hidden=True)]
    finish(state,tiles,units,"Ottomans","Byzantines","Constantinople: land walls, city interior, sea approaches, bombards, and siege works.",deploy=7,logistics=120,enemy_morale=110)

def generic_setup(state,key):
    data={
        "cannae":("Carthage","Rome","Hannibal","Paullus","Cannae: concave center, strong wings, and open cavalry ground.","prepared"),
        "kalka":("Mongols","Rus Coalition","Subutai","Mstislav","Kalka River: crossings, steppe pursuit lanes, and feigned retreat space.","river"),
        "cowpens":("Patriots","Britain","Daniel Morgan","Tarleton","Cowpens: layered lines, wooded flanks, and counterattack ground.","prepared"),
        "ulm":("France","Austria","Napoleon","Mack","Ulm: roads, river crossings, and encirclement corridors.","road"),
        "midway":("US Navy","Japan","Nimitz HQ","Yamamoto","Midway: ocean search grid, carrier groups, and island airfield.","sea"),
        "teutoburg":("Germanic Tribes","Rome","Arminius","Varus","Teutoburg: forest road ambush and broken marching terrain.","forest"),
        "thermopylae":("Greek Allies","Persia","Leonidas","Xerxes","Thermopylae: narrow pass, heights, and restricted frontage.","rough"),
        "stalingrad":("Soviets","Germany","Zhukov","Paulus","Stalingrad: urban ruins, river crossings, and encirclement objectives.","city"),
        "redcliffs":("Wu-Shu Alliance","Wei","Zhou Yu","Cao Cao","Red Cliffs: river fleet battle, fire ships, and chained enemy vessels.","river"),
        "tenochitlan":("Spanish Alliance","Aztec Empire","Cortes","Cuauhtemoc","Tenochtitlan: causeways, lake approaches, city districts, and allied entry points.","city"),
    }
    player,enemy,pname,ename,msg,theme=data[key]
    tiles=make_tiles("sea" if key in ["midway","redcliffs"] else "plain")
    if key=="midway": rect(tiles,1,3,6,9,"airfield"); pts(tiles,[(10,6),(12,8),(14,7)],"objective")
    elif key=="redcliffs": rect(tiles,1,3,6,9,"supply"); rect(tiles,18,22,6,9,"prepared"); pts(tiles,[(9,6),(10,7),(11,8)],"objective")
    elif key=="teutoburg": tiles=make_tiles("forest"); pts(tiles,[(4,7),(5,7),(6,8),(7,8),(8,8),(9,9),(10,9),(11,9)],"road"); rect(tiles,8,13,5,10,"rough")
    elif key=="thermopylae": rect(tiles,7,9,3,12,"rough"); rect(tiles,9,10,6,9,"bridge"); rect(tiles,4,6,4,11,"heights")
    elif key=="stalingrad": rect(tiles,6,15,3,12,"city"); rect(tiles,4,5,3,12,"river"); pts(tiles,[(5,6),(5,9)],"bridge")
    elif key=="tenochitlan": rect(tiles,6,8,2,13,"river"); pts(tiles,[(7,5),(7,8),(7,11)],"bridge"); rect(tiles,10,16,4,11,"city")
    else: rect(tiles,7,12,5,10,theme); pts(tiles,[(13,7),(14,7),(15,8)],"objective"); pts(tiles,[(5,5),(6,5),(17,10)],"forest")
    rect(tiles,1,3,6,9,"supply"); reveal_left(tiles,7)
    fast="aircraft" if key=="midway" else ("naval" if key in ["redcliffs","tenochitlan"] else "cavalry")
    units=commander_pair(player,enemy,pname,ename)+add_standard_units(player,enemy,"naval" if key in ["midway","redcliffs","tenochitlan"] else "infantry",fast,"artillery")
    finish(state,tiles,units,player,enemy,msg,deploy=7,logistics=105)

def setup_cannae(state): generic_setup(state,"cannae")
def setup_kalka(state): generic_setup(state,"kalka")
def setup_cowpens(state): generic_setup(state,"cowpens")
def setup_ulm(state): generic_setup(state,"ulm")
def setup_midway(state): generic_setup(state,"midway")
def setup_teutoburg(state): generic_setup(state,"teutoburg")
def setup_thermopylae(state): generic_setup(state,"thermopylae")
def setup_stalingrad(state): generic_setup(state,"stalingrad")
def setup_redcliffs(state): generic_setup(state,"redcliffs")
def setup_tenochitlan(state): generic_setup(state,"tenochitlan")

def register_content(state):
    state.principles=[
        Principle("principle1","1. Laying Plans / Strategic Assessment","Know terrain, enemy disposition, logistics, morale, timing, and likely enemy moves before committing."),
        Principle("principle2","2. Waging War / Economy of Force","Win quickly, avoid prolonged attrition, preserve resources, and use only the force required."),
        Principle("principle3","3. Attack by Stratagem / Win Before Fighting","Shape the battlefield before combat through positioning, deception, engineering, morale pressure, and blockade."),
        Principle("principle4","4. Tactical Dispositions / Defensive Positioning","Make defeat impossible first, then wait for the enemy to expose victory."),
        Principle("principle5","5. Energy / Directed Force","Use timing, momentum, reserves, and concentrated force."),
        Principle("principle6","6. Weak Points and Strong","Avoid strength, strike weakness."),
        Principle("principle7","7. Maneuvering","Win by movement, speed, deception, and positional advantage."),
        Principle("principle8","8. Variation in Tactics","Adapt to changing conditions."),
        Principle("principle9","9. Army on the March","Read movement, formation, terrain, and enemy behavior."),
        Principle("principle10","10. Terrain","Use ground, chokepoints, distance, and access routes as weapons."),
        Principle("principle11","11. The Nine Situations","Understand the psychological and strategic condition of the army."),
        Principle("principle12","12. Attack by Fire","Use fire, disruption, timing, and environmental shock."),
        Principle("principle13","13. Use of Spies / Intelligence","Exploit intelligence, local knowledge, informants, deception, and reconnaissance."),
    ]
    state.scenarios=[
        Scenario("gaugamela","principle1","Gaugamela, 331 BC","Alexander vs. Darius","Prepared Persian plain, chariot lanes, elephants, and exposed wings.","Macedon","Persia",setup_gaugamela),
        Scenario("normaninv","principle1","Normandy Invasion, 1944","Allied landings vs. German coastal defense","Beaches, bunkers, bocage, bridges, villages, and inland reserves.","Allies","Germany",setup_normaninv),
        Scenario("sixdaywar","principle2","Six-Day War, 1967","Israel vs. Egyptian forces","Desert maneuver, airfields, armor thrusts, and rapid objectives.","Israel","Egypt",setup_sixdaywar),
        Scenario("austerlitz","principle3","Austerlitz, 1805","Napoleon vs. Third Coalition","Pratzen Heights, frozen ponds, villages, and a deliberately weakened flank.","France","Coalition",setup_austerlitz),
        Scenario("yorktown","principle3","Yorktown, 1781","Washington and Rochambeau vs. Cornwallis","Peninsula, siege lines, redoubts, York River, and French naval blockade.","Allies","Britain",setup_yorktown),
        Scenario("constantinople","principle3","Fall of Constantinople, 1453","Mehmed II vs. Byzantine defenders","Land walls, city interior, sea approaches, bombards, and siege pressure.","Ottomans","Byzantines",setup_constantinople),
        Scenario("cannae","principle4","Cannae, 216 BC","Hannibal vs. Rome","Concave center, strong wings, and open cavalry ground.","Carthage","Rome",setup_cannae),
        Scenario("kalka","principle5","Kalka River, 1223","Subutai vs. Rus Coalition","River crossing, steppe pursuit lanes, and feigned retreat space.","Mongols","Rus Coalition",setup_kalka),
        Scenario("cowpens","principle6","Cowpens, 1781","Daniel Morgan vs. Tarleton","Layered defensive lines, wooded flanks, and counterattack ground.","Patriots","Britain",setup_cowpens),
        Scenario("ulm","principle7","Ulm Campaign, 1805","Napoleon vs. Mack","Roads, river crossings, and encirclement corridors.","France","Austria",setup_ulm),
        Scenario("midway","principle8","Midway, 1942","US Navy vs. Imperial Japan","Ocean search grid, carrier air groups, and island airfield.","US Navy","Japan",setup_midway),
        Scenario("teutoburg","principle9","Teutoburg Forest, AD 9","Arminius vs. Varus","Forest road ambush and broken marching terrain.","Germanic Tribes","Rome",setup_teutoburg),
        Scenario("thermopylae","principle10","Thermopylae, 480 BC","Greek Allies vs. Persia","Narrow pass, heights, and restricted frontage.","Greek Allies","Persia",setup_thermopylae),
        Scenario("stalingrad","principle11","Stalingrad, 1942","Soviets vs. Germany","Urban ruins, Volga crossings, and encirclement objectives.","Soviets","Germany",setup_stalingrad),
        Scenario("redcliffs","principle12","Red Cliffs, 208","Wu-Shu Alliance vs. Cao Cao","River fleet battle, fire ships, and chained enemy vessels.","Wu-Shu Alliance","Wei",setup_redcliffs),
        Scenario("tenochitlan","principle13","Siege of Tenochtitlan, 1521","Spanish-Tlaxcalan Alliance vs. Aztec Empire","Causeways, lake approaches, city districts, and allied entry points.","Spanish Alliance","Aztec Empire",setup_tenochitlan),
    ]


